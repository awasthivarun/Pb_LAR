#!/usr/bin/env python3
"""Read-only Pb_LAR calculation inventory with an editable scientific review ledger.

Examples:
  python scripts/calculation_ledger.py scan
  python scripts/calculation_ledger.py scan --sacct
  python scripts/calculation_ledger.py seed
  python scripts/calculation_ledger.py submit N19 --slurm-id 60040944
  python scripts/calculation_ledger.py review X90 --status validated --priority core \
      --summary 'Two separate on-top adsorbed H atoms remain after relaxation.'
  python scripts/calculation_ledger.py show N19
  python scripts/calculation_ledger.py stats

Never modifies calculation directories or their metadata.json files.
"""

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

HA_TO_EV = 27.211386245988
SOURCE_DEFAULT = Path('/pscratch/sd/a/awasthi/Pb_LAR_source')
DATA_DEFAULT = Path('/pscratch/sd/a/awasthi/Pb_LAR')
STATES = {'not_reviewed', 'provisional', 'validated', 'invalid', 'superseded'}
PRIORITIES = {'unassigned', 'core', 'supporting', 'diagnostic', 'low'}

# Retrospective interpretations from project discussions. Not a replacement for re-reading raw results.
SEED = {
    'N02': ('supporting', 'provisional',
        'Earlier fixed-potential two-H rearrangement: separated adsorption environments to two H atoms associated with one Pb atom. Dry/continuum-only model; numerical barrier and final chemistry require re-audit.'),
    'N03': ('supporting', 'provisional',
        'Earlier fixed-potential rearrangement from a shared-Pb hydrogen configuration toward a strongly displaced surface Pb-H configuration. Distinct from later fully detached hydrated PbH2 NEBs; re-audit barrier and structures.'),
    'N08': ('diagnostic', 'invalid', 'Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.'),
    'N09': ('diagnostic', 'invalid', 'Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.'),
    'N10': ('diagnostic', 'invalid', 'Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.'),
    'N11': ('diagnostic', 'invalid', 'Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.'),
    'N12': ('diagnostic', 'superseded', 'Hydrated HCP-adatom detachment path exposed a lower-energy precursor; subsequent independent precursor optimization and revised NEB supersede this reference.'),
    'N13': ('diagnostic', 'provisional', 'Hydrated FCC-adatom detachment at cathodic potential: geometries appeared intact but abrupt dielectric/charge change makes kinetic profile uncertain.'),
    'N14': ('core', 'provisional', 'Hydrated terrace PbH2 detachment at approximately -1.0 V RHE; converged nonclimbing NEB. Monotonically uphill, endpoint delta Omega approximately +1.309621 eV. Not a confirmed saddle-point barrier.'),
    'N15': ('diagnostic', 'invalid', 'Hydrated terrace PbH2 detachment at approximately -1.8 V RHE; anomalous negative grand potentials and hydrogen/water rearrangements. Endpoint thermodynamics remain separate and usable.'),
    'N16': ('core', 'provisional', 'Hydrated HCP-adatom PbH2 detachment at approximately -1.0 V RHE from independently relaxed lower-energy precursor. Converged nonclimbing NEB, monotonic uphill, endpoint delta Omega +0.880822 eV.'),
    'N17': ('diagnostic', 'superseded', 'First hydrated Tafel NEB (8 intermediates): timed out at about 0.134 eV/A; bonding region poorly resolved. Replaced by refined 16-image path.'),
    'N18': ('supporting', 'provisional', 'Hydrated Tafel NEB with 16 intermediates converged at 0.0701 eV/A. Sampled maximum +0.238992 eV relative to original hollow-like two-H state. Found lower-energy on-top-like reactant.'),
    'N19': ('core', 'provisional', 'Endpoint-consistent hydrated Tafel NEB (8 intermediates) at approximately -1.0 V RHE: sampled maximum +0.512562 eV, reaction delta Omega -0.984956 eV relative to independently relaxed on-top two-H state. Force 0.067 eV/A at step zero; not climbing-image or independently rediscovered MEP.'),
    'X86': ('supporting', 'validated', 'Independent relaxation found an intact hydrated HCP-adatom PbH2 precursor approximately 0.328 eV below the original precursor. Forms starting state of revised adatom detachment NEB.'),
    'X87': ('core', 'validated', 'Hydrated terrace two-adsorbed-H endpoint used for initial Tafel study, two explicit waters intact. Grand potential -2168.783260308874 Ha; later superseded as lowest reactant by an on-top-like configuration.'),
    'X88': ('supporting', 'validated', 'Hydrated molecular-H2 endpoint, two explicit waters intact. Grand potential -2168.827300135164 Ha; vertically oriented alternative was found lower.'),
    'X89': ('diagnostic', 'validated', 'Single-point hydration stress test of a formerly pathological dry H configuration: grand potential +2.566864 eV relative to the hydrated two-H reactant. Off-path diagnostic, NOT an activation barrier.'),
    'X90': ('core', 'validated', 'Independent relaxation of lower-energy on-top-like reactant: two separately adsorbed H atoms remain; final force 0.037538 eV/A. About 0.273 eV below original hydrated Tafel reactant. Final G should be read from its own Ecomponents.'),
    'X91': ('supporting', 'validated', 'Independent relaxation of nearly vertical H2 product: initial maximum force already 0.028671 eV/A; about 0.060 eV lower than original H2 product. Final G should be read from its own Ecomponents.'),
    'X28': ('core', 'validated', 'Terrace PbH2 detachment product at approximately -1.0 V RHE; relative to matched hydrated precursor X21: +1.309621 eV endpoint grand potential.'),
    'X30': ('supporting', 'validated', 'Terrace PbH2 detachment product at approximately -1.2 V RHE; relative to matched precursor X25: +1.318411 eV.'),
    'X31': ('supporting', 'validated', 'Terrace PbH2 detachment product at approximately -1.4 V RHE; relative to matched precursor X26: +1.356592 eV.'),
    'X29': ('supporting', 'validated', 'Terrace PbH2 detachment product at approximately -1.6 V RHE; relative to matched precursor X22: +1.432054 eV.'),
    'X32': ('supporting', 'validated', 'Terrace PbH2 detachment product at approximately -1.8 V RHE; relative to matched precursor X27: +1.554947 eV.'),
}


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def read_json(path):
    try:
        return json.loads(path.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f'Cannot parse JSON: {path}: {exc}') from exc


def save_if_changed(path, data):
    serialized = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + '\n'
    if path.is_file() and path.read_text() == serialized:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', dir=path.parent, prefix=f'.{path.name}.', delete=False) as tmp:
        tmp.write(serialized)
        temporary = Path(tmp.name)
    os.replace(temporary, path)
    return True


def save_text_if_changed(path, content):
    if path.is_file() and path.read_text() == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile('w', dir=path.parent, prefix=f'.{path.name}.', delete=False) as tmp:
        tmp.write(content)
        temporary = Path(tmp.name)
    os.replace(temporary, path)
    return True


def relative_job_directory(path, root):
    if not isinstance(path, str) or not path.strip():
        return None
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = root / candidate
    try:
        rel = candidate.resolve().relative_to(root.resolve())
    except ValueError:
        return None
    return rel.as_posix() if rel != Path('.') else None


def manifest_links(source, root):
    by_path = defaultdict(list)
    for manifest in sorted((source / 'campaigns').glob('*.json')):
        try:
            content = read_json(manifest)
        except RuntimeError as exc:
            print(f'WARNING: {exc}', file=sys.stderr)
            continue
        def visit(item):
            if isinstance(item, dict):
                job = item.get('job_id')
                directory = next((item[k] for k in ('directory', 'relpath', 'job_dir')
                                  if isinstance(item.get(k), str)), None)
                rel = relative_job_directory(directory, root)
                if rel and job:
                    by_path[rel].append({'job_id': str(job), 'manifest': str(manifest.relative_to(source))})
                for value in item.values():
                    visit(value)
            elif isinstance(item, list):
                for value in item:
                    visit(value)
        visit(content)
    return by_path


def scientific_family(path, metadata):
    if metadata.get('family'):
        return str(metadata['family'])
    text = path.lower()
    if 'tafel' in text or '/her/' in text:
        return 'HER / Tafel'
    if 'pbh2' in text or 'hydride' in text:
        return 'PbH2-related'
    if 'adatom' in text or 'vacancy' in text or 'defect' in text:
        return 'surface defects'
    if 'adsorption' in text or 'h2_candidate' in text:
        return 'hydrogen adsorption'
    return 'unclassified'


def latest_component_value(path, key):
    if not path.is_file():
        return None
    result = None
    for line in path.read_text(errors='replace').splitlines():
        tokens = line.split()
        if len(tokens) >= 3 and tokens[0] == key and tokens[1] == '=':
            try:
                result = float(tokens[2])
            except ValueError:
                pass
    return result


def last_fire(path):
    if not path.is_file():
        return None
    lines = path.read_text(errors='replace').splitlines()
    for line in reversed(lines):
        match = re.search(r'FIRE:\s*(\d+)\s+\S+\s+([-+\d.eE]+)\s+([-+\d.eE]+)', line)
        if match:
            return {'step': int(match.group(1)), 'ase_energy_eV': float(match.group(2)),
                    'fmax_eV_A': float(match.group(3))}
    return None


def find_components(folder, preferred):
    candidate = folder / preferred
    if candidate.is_file():
        return candidate
    matches = sorted(folder.glob('*Ecomponents'))
    return matches[-1] if matches else None


def file_hashes(folder):
    result = {}
    for filename in ('go.py', 'neb.py', 'sp.py', 'vib.py', 'dimer.py', 'submit.sh', 'POSCAR'):
        path = folder / filename
        if path.is_file():
            result[filename] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


def slurm_ids(folder):
    ids = set()
    for entry in folder.iterdir():
        if not entry.is_file():
            continue
        if re.fullmatch(r'(?:go|neb|sp|vib|dimer|slurm)[.-](\d+)(?:\.out)?', entry.name):
            match = re.search(r'(\d+)', entry.name)
            ids.add(match.group(1))
    return sorted(ids, key=int)


def get_calc_type(folder, metadata):
    for kind, name in [('neb', 'neb.py'), ('go', 'go.py'), ('sp', 'sp.py'),
                       ('vib', 'vib.py'), ('dimer', 'dimer.py')]:
        if (folder / name).is_file():
            return kind
    if metadata.get('n_intermediate_images') is not None or metadata.get('intermediate_images') is not None:
        return 'neb'
    if metadata.get('family') == 'bulk_reference':
        return 'bulk_reference'
    return 'unknown'


def extract_results(folder, kind, metadata):
    results = {'slurm_ids': slurm_ids(folder)}
    mu = metadata.get('target_mu_Ha')
    energy_key = metadata.get('endpoint_energy_key') or metadata.get('endpoint_energy_label')
    if energy_key not in ('G', 'F'):
        energy_key = 'G' if mu is not None else 'F'
    results['energy_key'] = energy_key
    if kind == 'neb':
        enddirs = sorted(p for p in folder.iterdir() if p.is_dir() and re.fullmatch(r'\d\d', p.name))
        profile = []
        n_expected = metadata.get('n_intermediate_images', metadata.get('intermediate_images',
                                                   metadata.get('nimages')))
        if n_expected is None and (folder / 'neb.py').is_file():
            match = re.search(r'(?m)^NIMAGES\s*=\s*(\d+)', (folder / 'neb.py').read_text())
            if match:
                n_expected = int(match.group(1))
        if n_expected is not None:
            n_expected = int(n_expected)
        for image_dir in enddirs:
            number = int(image_dir.name)
            is_endpoint = number == 0 or (n_expected is not None and number == n_expected + 1)
            components = find_components(image_dir, 'endpoint.Ecomponents' if is_endpoint else 'job.Ecomponents')
            energy = latest_component_value(components, energy_key) if components else None
            profile.append({'image': number, f'{energy_key}_Ha': energy,
                            'geometry_present': (image_dir / 'CONTCAR').is_file()})
        results['image_profile'] = profile
        values = [p.get(f'{energy_key}_Ha') for p in profile]
        if (n_expected is not None and len(values) == n_expected + 2
                and all(p['image'] == i for i, p in enumerate(profile))
                and all(value is not None for value in values)):
            initial = values[0]
            results['sampled_forward_barrier_eV'] = round((max(values) - initial) * HA_TO_EV, 6)
            difference_key = 'endpoint_delta_omega_eV' if energy_key == 'G' else 'endpoint_delta_f_eV'
            results[difference_key] = round((values[-1] - initial) * HA_TO_EV, 6)
            results['maximum_image'] = profile[values.index(max(values))]['image']
        results['optimizer'] = last_fire(folder / 'neb.log')
    else:
        components = find_components(folder, 'job.Ecomponents')
        if components:
            for component in ('G', 'F', 'muN', 'A_diel'):
                value = latest_component_value(components, component)
                if value is not None:
                    results[component + '_Ha'] = value
        results['optimizer'] = last_fire(folder / 'opt.log')
        results['final_geometry_present'] = (folder / 'CONTCAR').is_file()
    return results


def get_scheduler_states(ids):
    states = {}
    for start in range(0, len(ids), 100):
        subset = ids[start:start + 100]
        try:
            completed = subprocess.run([
                'sacct', '-n', '-X', '-P', '-j', ','.join(subset),
                '--format=JobID,State,ExitCode,Elapsed'], text=True, capture_output=True, timeout=30)
        except (FileNotFoundError, subprocess.TimeoutExpired):
            print('WARNING: sacct unavailable; scheduler states left as recorded.', file=sys.stderr)
            return states
        if completed.returncode != 0:
            print(f'WARNING: sacct failed: {completed.stderr.strip()}', file=sys.stderr)
            return states
        for line in completed.stdout.splitlines():
            fields = line.strip().split('|')
            if len(fields) >= 4 and fields[0].isdigit():
                states[fields[0]] = {'state': fields[1], 'exit_code': fields[2], 'elapsed': fields[3]}
    return states


def fresh_ledger(root):
    return {'schema_version': 1, 'data_root': str(root), 'jobs': {}, 'unmatched_retrospective_notes': {}}


def load_ledger(path, root):
    if not path.is_file():
        return fresh_ledger(root)
    ledger = read_json(path)
    if ledger.get('schema_version') != 1 or not isinstance(ledger.get('jobs'), dict):
        raise RuntimeError('Unknown ledger schema; refuse to modify.')
    if Path(ledger.get('data_root', '')).resolve() != root.resolve():
        raise RuntimeError('Ledger data_root differs from requested --data-root.')
    return ledger


def scan(ledger, root, source, use_sacct):
    manifest_index = manifest_links(source, root)
    candidates = {}
    for meta in root.rglob('metadata.json'):
        candidates[meta.parent.resolve()] = meta.parent
    for script_name in ('go.py', 'neb.py', 'sp.py', 'vib.py', 'dimer.py'):
        for script in root.rglob(script_name):
            candidates[script.parent.resolve()] = script.parent
    for directory in manifest_index:
        path = root / directory
        if path.is_dir() and any((path / filename).exists() for filename in
                                    ('metadata.json', 'submit.sh', 'POSCAR', 'CONTCAR', 'neb.log', 'job.Ecomponents')):
            candidates[path.resolve()] = path
    all_ids = set()
    job_count = 0
    for folder in sorted(candidates.values()):
        relative = str(folder.relative_to(root))
        old = ledger['jobs'].get(relative, {})
        meta_file = folder / 'metadata.json'
        meta = read_json(meta_file) if meta_file.is_file() else {}
        if not isinstance(meta, dict):
            print(f'WARNING: skipping non-object metadata: {meta_file}', file=sys.stderr)
            continue
        manifest = manifest_index.get(relative, [])
        jobid = meta.get('job_id') or (manifest[0]['job_id'] if manifest else None)
        kind = get_calc_type(folder, meta)
        # A scan without --sacct must not discard Slurm history obtained by an earlier scan.
        results = extract_results(folder, kind, meta)
        prior_scheduler = old.get('results', {}).get('scheduler', {})
        if prior_scheduler:
            results['scheduler'] = dict(prior_scheduler)
        record = dict(old)
        record.update({
            'file_sha256': file_hashes(folder),
            'job_id': str(jobid) if jobid else None,
            'directory': relative,
            'calculation_type': kind,
            'family': scientific_family('/' + relative, meta),
            'setup': meta,
            'setup_metadata_path': str(meta_file.relative_to(root)) if meta_file.is_file() else None,
            'manifests': manifest,
            'results': results,
        })
        record.setdefault('scientific_review', {'status': 'not_reviewed', 'priority': 'unassigned', 'history': []})
        ledger['jobs'][relative] = record
        all_ids.update(record['results']['slurm_ids'])
        all_ids.update(str(event['slurm_id']) for event in record.get('execution_events', [])
                       if event.get('slurm_id'))
        job_count += 1
    if use_sacct and all_ids:
        statuses = get_scheduler_states(sorted(all_ids, key=int))
        for item in ledger['jobs'].values():
            ids = set(item.get('results', {}).get('slurm_ids', []))
            ids.update(str(event['slurm_id']) for event in item.get('execution_events', [])
                       if event.get('slurm_id'))
            scheduler = item['results'].setdefault('scheduler', {})
            scheduler.update({id_: statuses[id_] for id_ in ids if id_ in statuses})
    # Preserve historical entries whose directories disappeared; mark missing instead of deleting them.
    for path, item in ledger['jobs'].items():
        item['directory_currently_present'] = (root / path).is_dir()
    return job_count


def record_submission(ledger, job_name, slurm_id, note):
    path = find_job(ledger, job_name)
    job = ledger['jobs'][path]
    events = job.setdefault('execution_events', [])
    if any(str(item.get('slurm_id')) == str(slurm_id) for item in events):
        return False
    events.append({'event': 'submitted', 'slurm_id': str(slurm_id),
                   'recorded_utc': utc_now(), 'note': note})
    return True


def find_job(ledger, name):
    if name in ledger['jobs']:
        return name
    matches = [key for key, job in ledger['jobs'].items() if job.get('job_id') == name]
    if not matches:
        raise ValueError(f'No job found for {name}. Run scan; inspect unmatched notes if relevant.')
    if len(matches) > 1:
        raise ValueError(f'Ambiguous job ID {name}; use directory path: {matches}')
    return matches[0]


def review(ledger, job_name, status, priority, summary, caveats, source):
    path = find_job(ledger, job_name)
    job = ledger['jobs'][path]
    info = job.setdefault('scientific_review', {'status': 'not_reviewed', 'priority': 'unassigned', 'history': []})
    history = info.setdefault('history', [])
    entry = {'recorded_utc': utc_now(), 'source': source, 'assessment': summary, 'limitations': caveats}
    if history and all(history[-1].get(k) == entry[k] for k in ('source', 'assessment', 'limitations')) and \
            info.get('status') == status and info.get('priority') == priority:
        return False
    history.append(entry)
    info['status'] = status
    info['priority'] = priority
    return True


def seed(ledger):
    done = 0
    missing = {}
    for jobid, (priority, status, note) in SEED.items():
        try:
            path = find_job(ledger, jobid)
        except ValueError:
            missing[jobid] = {'priority': priority, 'status': status, 'assessment': note}
            continue
        info = ledger['jobs'][path]['scientific_review']
        if info['history']:
            continue
        if review(ledger, path, status, priority, note,
                  'Retrospective from discussion; verify raw files before publication.', 'conversation_reconstruction'):
            done += 1
    ledger['unmatched_retrospective_notes'] = missing
    return done, len(missing)


def md_escape(value):
    return str(value or '').replace('|', '\\|').replace('\n', ' ').strip()


def make_report(ledger):
    jobs = list(ledger['jobs'].values())
    sections = defaultdict(list)
    for job in jobs:
        sections[job.get('family') or 'unclassified'].append(job)
    lines = [
        '# Pb_LAR calculation ledger', '',
        'Generated from `calculation_ledger.json`. Edit reviews with `scripts/calculation_ledger.py review`.',
        'Raw DFT data and original `metadata.json` files remain in the separate Pb_LAR calculation tree.',
        '**A `COMPLETED` Slurm state is not equivalent to geometry/NEB convergence or scientific validation.**', '',
        f'Jobs indexed: **{len(jobs)}**; job records awaiting scientific review: '
        f'**{sum(j["scientific_review"]["status"] == "not_reviewed" for j in jobs)}**.', ''
    ]
    for family in sorted(sections):
        lines.extend([f'## {family}', '',
                      '| ID | Type | Scientific status | Priority | Setup purpose | Directory |',
                      '|---|---|---|---|---|---|'])
        for job in sorted(sections[family], key=lambda j: (j.get('job_id') or 'ZZZ', j['directory'])):
            r = job['scientific_review']
            purpose = job['setup'].get('purpose') or job['setup'].get('description') or '(not recorded)'
            lines.append('| ' + ' | '.join(map(md_escape, (
                job.get('job_id') or '(no ID)', job.get('calculation_type'), r.get('status'),
                r.get('priority'), purpose, '`' + job['directory'] + '`'))) + ' |')
        lines.append('')
    lines.extend(['## Scientific notes', ''])
    for job in sorted(jobs, key=lambda j: (j.get('job_id') or 'ZZZ', j['directory'])):
        r = job['scientific_review']
        if not r.get('history'):
            continue
        lines.extend([f'### {job.get("job_id") or job["directory"]}', '',
                      f'**Location:** `{job["directory"]}`. **Priority:** {r["priority"]}. '
                      f'**Review state:** {r["status"]}.', ''])
        purpose = job['setup'].get('purpose') or job['setup'].get('description')
        if purpose:
            lines.extend([f'**Setup intent:** {purpose}', ''])
        last = r['history'][-1]
        lines.extend([f'**Assessment:** {last["assessment"]}', ''])
        if last.get('limitations'):
            lines.extend([f'**Caveats:** {last["limitations"]}', ''])
        results = job.get('results', {})
        if 'sampled_forward_barrier_eV' in results:
            caution = ' (INVALID PATH; NOT A PHYSICAL BARRIER)' if r.get('status') == 'invalid' else ''
            lines.extend([f'**Extracted sampled maximum{caution}:** {results["sampled_forward_barrier_eV"]:+.6f} eV; '
                          f'**endpoint difference:** {results.get("endpoint_delta_omega_eV", results.get("endpoint_delta_f_eV")):+.6f} eV '
                          f'({results["energy_key"]}).', ''])
    if ledger.get('unmatched_retrospective_notes'):
        lines.extend(['## Unmatched retrospective notes', '',
                      'These ID-level recollections could not be linked to a current calculation folder; '
                      'they must not be treated as verified records.', ''])
        for jid, item in sorted(ledger['unmatched_retrospective_notes'].items()):
            lines.extend([f'**{jid}:** {item["assessment"]}', ''])
    return '\n'.join(lines).rstrip() + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--data-root', type=Path, default=DATA_DEFAULT)
    parser.add_argument('--source-root', type=Path, default=SOURCE_DEFAULT)
    sub = parser.add_subparsers(dest='command', required=True)
    scan_arg = sub.add_parser('scan', help='Import all jobs; update observed outputs, preserve reviews')
    scan_arg.add_argument('--sacct', action='store_true', help='Also query Slurm for any discovered job IDs')
    sub.add_parser('seed', help='Attach conservative historical notes from this project conversation')
    submit_arg = sub.add_parser('submit', help='Record a Slurm job ID immediately after sbatch')
    submit_arg.add_argument('job', help='Job ID or directory path')
    submit_arg.add_argument('--slurm-id', required=True, help='Numeric Slurm job ID')
    submit_arg.add_argument('--note', default='')
    review_arg = sub.add_parser('review', help='Record a human scientific interpretation')
    review_arg.add_argument('job', help='Job ID or directory path')
    review_arg.add_argument('--status', choices=sorted(STATES), required=True)
    review_arg.add_argument('--priority', choices=sorted(PRIORITIES), required=True)
    review_arg.add_argument('--summary', required=True)
    review_arg.add_argument('--caveats', default='')
    review_arg.add_argument('--source', default='user_review')
    show_arg = sub.add_parser('show', help='Print one full ledger entry')
    show_arg.add_argument('job')
    sub.add_parser('stats', help='Summarize inventory and review progress')
    args = parser.parse_args()
    root, source = args.data_root.resolve(), args.source_root.resolve()
    path = source / 'calculation_ledger.json'
    report = source / 'calculation_ledger.md'
    if not root.is_dir():
        parser.error(f'Data root missing: {root}')
    if not source.is_dir():
        parser.error(f'Source root missing: {source}')
    ledger = load_ledger(path, root)
    if args.command == 'scan':
        count = scan(ledger, root, source, args.sacct)
        print(f'Indexed {count} current calculation directories, {len(ledger["jobs"])} total retained records.')
    elif args.command == 'seed':
        applied, unmatched = seed(ledger)
        print(f'Added {applied} retrospective reviews; {unmatched} notes await a matching job directory.')
    elif args.command == 'submit':
        if not args.slurm_id.isdigit():
            parser.error('--slurm-id must be numeric')
        changed = record_submission(ledger, args.job, args.slurm_id, args.note)
        print('Submission recorded.' if changed else 'Submission already recorded.')
    elif args.command == 'review':
        changed = review(ledger, args.job, args.status, args.priority, args.summary, args.caveats, args.source)
        print('Scientific review appended.' if changed else 'Identical review already current.')
    elif args.command == 'show':
        print(json.dumps(ledger['jobs'][find_job(ledger, args.job)], indent=2))
        return
    elif args.command == 'stats':
        counts = Counter(j['scientific_review']['status'] for j in ledger['jobs'].values())
        print('Jobs:', len(ledger['jobs']))
        print('Review statuses:', dict(counts))
        print('Unmatched retrospective IDs:', sorted(ledger.get('unmatched_retrospective_notes', {})))
        return
    updated = save_if_changed(path, ledger)
    report_updated = save_text_if_changed(report, make_report(ledger))
    print(f'Ledger: {path} (changed={updated})')
    print(f'Readable report: {report} (changed={report_updated})')


if __name__ == '__main__':
    main()
