# Pb_LAR calculation ledger

Generated from `calculation_ledger.json`. Edit reviews with `scripts/calculation_ledger.py review`.
Raw DFT data and original `metadata.json` files remain in the separate Pb_LAR calculation tree.
**A `COMPLETED` Slurm state is not equivalent to geometry/NEB convergence or scientific validation.**

Jobs indexed: **152**; job records awaiting scientific review: **127**.

## HER / Tafel

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| X89 | sp | validated | diagnostic | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/hydrated_N08_image05_sp` |

## HER_Tafel_explicit_water

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| N17 | neb | superseded | diagnostic | `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2_explicit_water` |
| N18 | neb | provisional | supporting | `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2_explicit_water_refined16` |
| N19 | neb | provisional | core | `kinetics/Pb111/fixed_mu/m0p1193/Tafel_ontop2H_to_H2_explicit_water` |
| X87 | go | validated | core | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/hydrated_surface_2H` |
| X88 | go | validated | supporting | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/hydrated_H2_product` |
| X90 | go | validated | core | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/relax_2H_from_N18_image05` |
| X91 | go | validated | supporting | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/relax_H2_from_N18_image14` |

## NEB

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| N08 | neb | invalid | diagnostic | `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2` |
| N09 | neb | invalid | diagnostic | `kinetics/Pb111/fixed_mu/m0p11195/Tafel_surface2H_to_H2` |
| N10 | neb | invalid | diagnostic | `kinetics/Pb111/fixed_mu/m0p1046/Tafel_surface2H_to_H2` |
| N11 | neb | invalid | diagnostic | `kinetics/Pb111/fixed_mu/m0p09725/Tafel_surface2H_to_H2` |
| N12 | neb | superseded | diagnostic | `kinetics/Pb111/fixed_mu/m0p1193/adatom_hcp_PbH2_to_detached_explicit_water` |
| N13 | neb | provisional | diagnostic | `kinetics/Pb111/fixed_mu/m0p0899/adatom_fcc_PbH2_to_detached_explicit_water` |
| N14 | neb | provisional | core | `kinetics/Pb111/fixed_mu/m0p1193/terrace_PbH2_to_detached_explicit_water` |
| N15 | neb | invalid | diagnostic | `kinetics/Pb111/fixed_mu/m0p0899/terrace_PbH2_to_detached_explicit_water` |
| N16 | neb | provisional | core | `kinetics/Pb111/fixed_mu/m0p1193/adatom_hcp_PbH2_X86_to_X44_explicit_water` |

## PbH2_extraction

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| X01 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_2p5` |
| X02 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_4p0` |
| X03 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_6p0` |
| X04 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_2p5` |
| X05 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_4p0` |
| X06 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_6p0` |

## PbH2_extraction_explicit_water

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| X28 | go | validated | core | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p1193` |
| X29 | go | validated | supporting | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p09725` |
| X30 | go | validated | supporting | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p11195` |
| X31 | go | validated | supporting | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p1046` |
| X32 | go | validated | supporting | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p0899` |

## PbH2_potential_sweep

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| X08 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p11195` |
| X09 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p1046` |
| X10 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p09725` |
| X11 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p0899` |
| X12 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p11195` |
| X13 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p1046` |
| X14 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p09725` |
| X15 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p0899` |
| X16 | go | not_reviewed | unassigned | `surfaces/Pb111/PbH2_extraction/separation/fixed_mu/m0p1193/plus_1p5` |

## adatom_PbH2_explicit_water

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| X33 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p1193` |
| X34 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p1193` |
| X35 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p11195` |
| X36 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p11195` |
| X37 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p1046` |
| X38 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p1046` |
| X39 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p09725` |
| X40 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p09725` |
| X41 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p0899` |
| X42 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p0899` |
| X43 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p1193` |
| X44 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p1193` |
| X45 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p11195` |
| X46 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p11195` |
| X47 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p1046` |
| X48 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p1046` |
| X49 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p09725` |
| X50 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p09725` |
| X51 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p0899` |
| X52 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p0899` |
| X78 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p1193` |
| X79 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p11195` |
| X80 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p1046` |
| X81 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p09725` |
| X82 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p11195` |
| X83 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p1046` |
| X84 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p09725` |
| X85 | go | not_reviewed | unassigned | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p0899` |
| X86 | go | validated | supporting | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_from_N12_image01/m0p1193` |

## bulk_reference

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| B01 | unknown | not_reviewed | unassigned | `bulk/Pb_fcc` |

## clean

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| S01 | go | not_reviewed | unassigned | `surfaces/Pb111/clean` |

## convergence

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| S02 | go | not_reviewed | unassigned | `surfaces/Pb111/convergence/4L_k6` |
| S03 | go | not_reviewed | unassigned | `surfaces/Pb111/convergence/5L_k4` |
| S04 | go | not_reviewed | unassigned | `surfaces/Pb111/convergence/6L_k4` |

## defect

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| D01 | go | not_reviewed | unassigned | `surfaces/Pb111/defects/vacancy` |
| D02 | go | not_reviewed | unassigned | `surfaces/Pb111/defects/adatom_fcc` |
| D03 | go | not_reviewed | unassigned | `surfaces/Pb111/defects/adatom_hcp` |

## fixed_mu_1H

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| MH01 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p1193` |
| MH02 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p1046` |
| MH03 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p0899` |
| MH04 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p1193` |
| MH05 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p1046` |
| MH06 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p0899` |
| MH07 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p1193` |
| MH08 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p1046` |
| MH09 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p0899` |
| MH10 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p1193` |
| MH11 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p1046` |
| MH12 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p0899` |

## fixed_mu_2H

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| M2H01 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p1193` |
| M2H02 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p1046` |
| M2H03 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p0899` |
| M2H04 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p1193` |
| M2H05 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p1046` |
| M2H06 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p0899` |
| M2H07 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p1193` |
| M2H08 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p1046` |
| M2H09 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p0899` |
| X17 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_reference/separated/m0p11195` |
| X18 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_reference/same_Pb/m0p11195` |
| X19 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_reference/separated/m0p09725` |
| X20 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H2_reference/same_Pb/m0p09725` |

## fixed_mu_H2_endpoint

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| X53 | go | not_reviewed | unassigned | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1193/z4p0` |
| X54 | go | not_reviewed | unassigned | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1193/z6p0` |
| X55 | go | not_reviewed | unassigned | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p11195/z4p0` |
| X56 | go | not_reviewed | unassigned | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p11195/z6p0` |
| X57 | go | not_reviewed | unassigned | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1046/z4p0` |
| X58 | go | not_reviewed | unassigned | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1046/z6p0` |
| X59 | go | not_reviewed | unassigned | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p09725/z4p0` |
| X60 | go | not_reviewed | unassigned | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p09725/z6p0` |

## fixed_mu_clean

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| G01 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/clean/m0p1193` |
| G02 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/clean/m0p1046` |
| G03 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/clean/m0p0899` |
| X61 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/clean/m0p11195` |
| X62 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/clean/m0p09725` |

## fixed_mu_defect

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| X63 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p1193` |
| X64 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p11195` |
| X65 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p1046` |
| X66 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p09725` |
| X67 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p0899` |
| X68 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p1193` |
| X69 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p11195` |
| X70 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p1046` |
| X71 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p09725` |
| X72 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p0899` |
| X73 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p1193` |
| X74 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p11195` |
| X75 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p1046` |
| X76 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p09725` |
| X77 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p0899` |

## fixed_mu_neb

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| N01 | neb | not_reviewed | unassigned | `kinetics/Pb111/fixed_mu/m0p1193/surface_H_to_lifted_PbH` |
| N02 | neb | provisional | supporting | `kinetics/Pb111/fixed_mu/m0p1193/separated_2H_to_same_Pb` |
| N03 | neb | provisional | supporting | `kinetics/Pb111/fixed_mu/m0p1193/PbH2_surface_to_strongly_lifted` |
| N07 | neb | not_reviewed | unassigned | `kinetics/Pb111/fixed_mu/m0p1193/PbH2_strongly_lifted_to_detached` |

## neutral_1H

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| H01 | go | not_reviewed | unassigned | `surfaces/Pb111/H_adsorption/ontop` |
| H02 | go | not_reviewed | unassigned | `surfaces/Pb111/H_adsorption/bridge` |
| H03 | go | not_reviewed | unassigned | `surfaces/Pb111/H_adsorption/fcc` |
| H04 | go | not_reviewed | unassigned | `surfaces/Pb111/H_adsorption/hcp` |

## neutral_2H

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| HH01 | go | not_reviewed | unassigned | `surfaces/Pb111/H2_candidates/fcc_hcp` |
| HH02 | go | not_reviewed | unassigned | `surfaces/Pb111/H2_candidates/shared_bridges` |
| HH03 | go | not_reviewed | unassigned | `surfaces/Pb111/H2_candidates/PbH2_like` |

## neutral_neb

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| N04 | neb | not_reviewed | unassigned | `kinetics/Pb111/neutral/surface_H_to_deep_subsurface_H` |
| N05 | neb | not_reviewed | unassigned | `kinetics/Pb111/neutral/PbH2_surface_to_partially_extracted` |
| N06 | neb | not_reviewed | unassigned | `kinetics/Pb111/neutral/PbH2_partially_extracted_to_detached` |

## proton_well_rescue

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| X21 | go | not_reviewed | unassigned | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p1193` |
| X22 | go | not_reviewed | unassigned | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p09725` |
| X23 | go | not_reviewed | unassigned | `surfaces/Pb111/proton_well_rescue/proton_oriented/m0p1193` |
| X24 | go | not_reviewed | unassigned | `surfaces/Pb111/proton_well_rescue/proton_oriented/m0p09725` |
| X25 | go | not_reviewed | unassigned | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p11195` |
| X26 | go | not_reviewed | unassigned | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p1046` |
| X27 | go | not_reviewed | unassigned | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p0899` |

## subsurface_H

| ID | Type | Scientific status | Priority | Directory |
|---|---|---|---|---|
| SH01 | go | not_reviewed | unassigned | `surfaces/Pb111/H_subsurface/fcc` |
| SH02 | go | not_reviewed | unassigned | `surfaces/Pb111/H_subsurface/hcp` |
| SH03 | go | not_reviewed | unassigned | `surfaces/Pb111/H_subsurface/ontop` |
| X07 | go | not_reviewed | unassigned | `surfaces/Pb111/fixed_mu/H_subsurface/deep/m0p1193` |

## Scientific notes

### N02

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/separated_2H_to_same_Pb`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Grand-canonical NEB from two H atoms associated with different Pb atoms to the same-Pb Pb(H)2 surface state at target-mu = -0.1193 Ha.

**Assessment:** Earlier fixed-potential two-H rearrangement: separated adsorption environments to two H atoms associated with one Pb atom. Dry/continuum-only model; numerical barrier and final chemistry require re-audit.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.046713 eV; **endpoint difference:** -0.078953 eV (G).

### N03

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/PbH2_surface_to_strongly_lifted`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Grand-canonical NEB from the mildly lifted same-Pb Pb(H)2 surface state to the strongly lifted incipient-extraction state at target-mu = -0.1193 Ha.

**Assessment:** Earlier fixed-potential rearrangement from a shared-Pb hydrogen configuration toward a strongly displaced surface Pb-H configuration. Distinct from later fully detached hydrated PbH2 NEBs; re-audit barrier and structures.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.093080 eV; **endpoint difference:** -0.033521 eV (G).

### N08

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2`. **Priority:** diagnostic. **Review state:** invalid.

**Setup intent:** Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential.

**Assessment:** Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.047877 eV; **endpoint difference:** -1.311886 eV (G).

### N09

**Location:** `kinetics/Pb111/fixed_mu/m0p11195/Tafel_surface2H_to_H2`. **Priority:** diagnostic. **Review state:** invalid.

**Setup intent:** Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential.

**Assessment:** Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.057843 eV; **endpoint difference:** -1.314591 eV (G).

### N10

**Location:** `kinetics/Pb111/fixed_mu/m0p1046/Tafel_surface2H_to_H2`. **Priority:** diagnostic. **Review state:** invalid.

**Setup intent:** Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential.

**Assessment:** Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.027063 eV; **endpoint difference:** -1.341106 eV (G).

### N11

**Location:** `kinetics/Pb111/fixed_mu/m0p09725/Tafel_surface2H_to_H2`. **Priority:** diagnostic. **Review state:** invalid.

**Setup intent:** Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential.

**Assessment:** Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.000000 eV; **endpoint difference:** -1.381863 eV (G).

### N12

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/adatom_hcp_PbH2_to_detached_explicit_water`. **Priority:** diagnostic. **Review state:** superseded.

**Setup intent:** Hydrated PbH2 extraction from a low-coordinate HCP Pb adatom at fixed electron chemical potential.

**Assessment:** Hydrated HCP-adatom detachment path exposed a lower-energy precursor; subsequent independent precursor optimization and revised NEB supersede this reference.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.552896 eV; **endpoint difference:** +0.552896 eV (G).

### N13

**Location:** `kinetics/Pb111/fixed_mu/m0p0899/adatom_fcc_PbH2_to_detached_explicit_water`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Hydrated PbH2 extraction from a low-coordinate FCC Pb adatom at fixed electron chemical potential.

**Assessment:** Hydrated FCC-adatom detachment at cathodic potential: geometries appeared intact but abrupt dielectric/charge change makes kinetic profile uncertain.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.946463 eV; **endpoint difference:** +0.946463 eV (G).

### N14

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/terrace_PbH2_to_detached_explicit_water`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Hydrated terrace PbH2 extraction at fixed electron chemical potential, providing the matched terrace control for the HCP-adatom extraction NEB N12.

**Assessment:** Hydrated terrace PbH2 detachment at approximately -1.0 V RHE; converged nonclimbing NEB. Monotonically uphill, endpoint delta Omega approximately +1.309621 eV. Not a confirmed saddle-point barrier.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +1.309621 eV; **endpoint difference:** +1.309621 eV (G).

### N15

**Location:** `kinetics/Pb111/fixed_mu/m0p0899/terrace_PbH2_to_detached_explicit_water`. **Priority:** diagnostic. **Review state:** invalid.

**Setup intent:** Hydrated terrace PbH2 extraction at fixed electron chemical potential, providing the matched terrace control for the FCC-adatom extraction NEB N13.

**Assessment:** Hydrated terrace PbH2 detachment at approximately -1.8 V RHE; anomalous negative grand potentials and hydrogen/water rearrangements. Endpoint thermodynamics remain separate and usable.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +1.554947 eV; **endpoint difference:** +1.554947 eV (G).

### N16

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/adatom_hcp_PbH2_X86_to_X44_explicit_water`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Hydrated HCP-adatom PbH2 extraction from independently relaxed X86 to X44.

**Assessment:** Hydrated HCP-adatom PbH2 detachment at approximately -1.0 V RHE from independently relaxed lower-energy precursor. Converged nonclimbing NEB, monotonic uphill, endpoint delta Omega +0.880822 eV.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.880822 eV; **endpoint difference:** +0.880822 eV (G).

### N17

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2_explicit_water`. **Priority:** diagnostic. **Review state:** superseded.

**Assessment:** First hydrated Tafel NEB (8 intermediates): timed out at about 0.134 eV/A; bonding region poorly resolved. Replaced by refined 16-image path.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.000000 eV; **endpoint difference:** -1.198385 eV (G).

### N18

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2_explicit_water_refined16`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Resolve the H-H bond-forming region of the N17 hydrated Tafel pathway.

**Assessment:** Hydrated Tafel NEB with 16 intermediates converged at 0.0701 eV/A. Sampled maximum +0.238992 eV relative to original hollow-like two-H state. Found lower-energy on-top-like reactant.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.238992 eV; **endpoint difference:** -1.198385 eV (G).

### N19

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/Tafel_ontop2H_to_H2_explicit_water`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Tafel recombination from independently optimized on-top surface H.

**Assessment:** Endpoint-consistent hydrated Tafel NEB (8 intermediates) at approximately -1.0 V RHE: sampled maximum +0.512562 eV, reaction delta Omega -0.984956 eV relative to independently relaxed on-top two-H state. Force 0.067 eV/A at step zero; not climbing-image or independently rediscovered MEP.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum:** +0.512562 eV; **endpoint difference:** -0.984956 eV (G).

### X28

**Location:** `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p1193`. **Priority:** core. **Review state:** validated.

**Setup intent:** Construct a detached PbH2 + vacancy product with two hydride-oriented explicit first-shell water molecules so that PbH2 detachment can be compared against the hydrated surface Pb(H)2 precursor at identical stoichiometry and target-mu.

**Assessment:** Terrace PbH2 detachment product at approximately -1.0 V RHE; relative to matched hydrated precursor X21: +1.309621 eV endpoint grand potential.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X29

**Location:** `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p09725`. **Priority:** supporting. **Review state:** validated.

**Setup intent:** Construct a detached PbH2 + vacancy product with two hydride-oriented explicit first-shell water molecules so that PbH2 detachment can be compared against the hydrated surface Pb(H)2 precursor at identical stoichiometry and target-mu.

**Assessment:** Terrace PbH2 detachment product at approximately -1.6 V RHE; relative to matched precursor X22: +1.432054 eV.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X30

**Location:** `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p11195`. **Priority:** supporting. **Review state:** validated.

**Setup intent:** Continue the physical hydrated detached PbH2 branch to complete the fixed-mu detachment curve.

**Assessment:** Terrace PbH2 detachment product at approximately -1.2 V RHE; relative to matched precursor X25: +1.318411 eV.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X31

**Location:** `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p1046`. **Priority:** supporting. **Review state:** validated.

**Setup intent:** Continue the physical hydrated detached PbH2 branch to complete the fixed-mu detachment curve.

**Assessment:** Terrace PbH2 detachment product at approximately -1.4 V RHE; relative to matched precursor X26: +1.356592 eV.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X32

**Location:** `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p0899`. **Priority:** supporting. **Review state:** validated.

**Setup intent:** Continue the physical hydrated detached PbH2 branch to complete the fixed-mu detachment curve.

**Assessment:** Terrace PbH2 detachment product at approximately -1.8 V RHE; relative to matched precursor X27: +1.554947 eV.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X86

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_from_N12_image01/m0p1193`. **Priority:** supporting. **Review state:** validated.

**Setup intent:** Independently relax N12 NEB image 01 to determine whether its 0.157 eV stabilization represents a physical lower-energy precursor.

**Assessment:** Independent relaxation found an intact hydrated HCP-adatom PbH2 precursor approximately 0.328 eV below the original precursor. Forms starting state of revised adatom detachment NEB.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X87

**Location:** `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/hydrated_surface_2H`. **Priority:** core. **Review state:** validated.

**Setup intent:** Validate hydrated Tafel HER endpoint before any new NEB.

**Assessment:** Hydrated terrace two-adsorbed-H endpoint used for initial Tafel study, two explicit waters intact. Grand potential -2168.783260308874 Ha; later superseded as lowest reactant by an on-top-like configuration.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X88

**Location:** `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/hydrated_H2_product`. **Priority:** supporting. **Review state:** validated.

**Setup intent:** Validate hydrated Tafel HER endpoint before any new NEB.

**Assessment:** Hydrated molecular-H2 endpoint, two explicit waters intact. Grand potential -2168.827300135164 Ha; vertically oriented alternative was found lower.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X89

**Location:** `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/hydrated_N08_image05_sp`. **Priority:** diagnostic. **Review state:** validated.

**Setup intent:** Test whether N08 image05 proton-well stabilization persists with explicit hydration.

**Assessment:** Single-point hydration stress test of a formerly pathological dry H configuration: grand potential +2.566864 eV relative to the hydrated two-H reactant. Off-path diagnostic, NOT an activation barrier.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X90

**Location:** `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/relax_2H_from_N18_image05`. **Priority:** core. **Review state:** validated.

**Setup intent:** Relax lower-energy, on-top-like surface-2H configuration.

**Assessment:** Independent relaxation of lower-energy on-top-like reactant: two separately adsorbed H atoms remain; final force 0.037538 eV/A. About 0.273 eV below original hydrated Tafel reactant. Final G should be read from its own Ecomponents.

**Caveats:** Retrospective from discussion; verify raw files before publication.

### X91

**Location:** `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/relax_H2_from_N18_image14`. **Priority:** supporting. **Review state:** validated.

**Setup intent:** Relax lower-energy, nearly vertical H2 product configuration.

**Assessment:** Independent relaxation of nearly vertical H2 product: initial maximum force already 0.028671 eV/A; about 0.060 eV lower than original H2 product. Final G should be read from its own Ecomponents.

**Caveats:** Retrospective from discussion; verify raw files before publication.
