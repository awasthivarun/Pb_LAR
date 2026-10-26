# Pb_LAR calculation ledger

Generated from `calculation_ledger.json`. Edit reviews with `scripts/calculation_ledger.py review`.
Raw DFT data and original `metadata.json` files remain in the separate Pb_LAR calculation tree.
**A `COMPLETED` Slurm state is not equivalent to geometry/NEB convergence or scientific validation.**

Jobs indexed: **153**; job records awaiting scientific review: **0**.

**Scientific review statuses:** validated 11, provisional 127, invalid 5, superseded 10, not_reviewed 0.

**Review scope:** All 152 jobs have a written, evidence-limited assessment. This is a metadata/energy/scheduler audit and retrospective discussion reconciliation, not a final independent structural or electronic-state validation.

## Project-wide scientific synthesis

**Common-reactant hydrated Tafel versus terrace hydride thermodynamics at -1.0 V RHE** (jobs: X90, X91, X21, X28, N14, N19)

At target mu -0.11930 Ha, the independently optimized hydrated on-top 2H state X90 is the common reference. Surface-bound terrace PbH2-like X21 is +0.305355 eV, terrace-displaced PbH2 X28 is +1.614976 eV, and molecular H2 X91 is -0.984956 eV relative to X90. The non-climbing Tafel path N19 has a sampled maximum +0.512562 eV relative to X90.

**Limitations:** These fixed-mu comparisons share nominal stoichiometry and hydration, but have different local water geometries and lack bulk-solution standard-state, thermal, and vibrational corrections. A terrace hydride-formation NEB connecting X90 to X21 remains missing in the hydrated model. Do not compare endpoint energies directly as rate constants.

**Low-coordinate Pb sites reduce local hydride detachment cost** (jobs: X21, X28, X86, X44, N14, N16)

For matched hydrated local processes at -1.0 V vs RHE, terrace PbH2 detachment costs +1.309621 eV, while detachment from an existing HCP Pb adatom costs +0.880822 eV. The local detachment energy reduction is 0.428799 eV.

**Limitations:** The comparison has different precursor morphology and Pb atom counts; it omits the energetic/kinetic cost of forming the adatom defect and cannot establish a net corrosion rate.

**Hydration avoids the tested dry Tafel proton-well catastrophe** (jobs: N08, N09, N10, N11, X89, N17, N18, N19)

The dry-model Tafel NEBs generated unphysical multi-eV stabilization of detached hydrogen. An explicit-water single-point at the problematic geometry X89 instead gave +2.566864 eV relative to the hydrated reactant. A subsequent hydrated NEB and endpoint-refined band sample a chemically plausible Tafel recombination sequence.

**Limitations:** Hydration is not a general proof of physical accuracy: other hydrated NEBs still exhibit proton-well problems, and electronic population/dielectric terms need inspection near bond formation.

**Potential-dependent continuum-only adsorption and detachment anomalies** (jobs: MH02, MH09, M2H02, M2H05, X04, X08, X09, X10, X12, X13, X14)

Nominally comparable one-/two-H configurations differ by approximately 7.2-7.5 eV at selected potentials despite small ionic forces. Early continuum-only detachment pairs show differences of approximately 15.7-16.9 eV at several potentials. A partially lifted PbH2 trial X04 is about 16.18 eV below its source precursor.

**Limitations:** These discrepancies may reflect different physical/electronic basins or solvation-cavity artifacts. Treat them as diagnostics until geometries, charge, electronic branches, and water/solvent settings have been reconciled; they are not validated adsorption or extraction energies.

**Incomplete kinetic network** (jobs: N02, N03, N14, N16, N19)

Earlier continuum-only NEBs screened separate-H to same-Pb rearrangement and initial PbH2 lifting. Hydrated detachment and on-top Tafel recombination have since been examined, but a hydrated X90-to-X21 surface hydride-formation path and proton-electron transfer HER elementary steps (Volmer/Heyrovsky) have not been demonstrated in this ledger.

**Limitations:** Do not infer selectivity or steady-state coverage from isolated pathway maxima. Missing molecular solution chemistry, pre-exponential factors, explicit proton donors, and electrochemical barriers must be considered in a consistent microkinetic framework.

## HER / Tafel

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X89 | sp | validated | diagnostic | Test whether N08 image05 proton-well stabilization persists with explicit hydration. | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/hydrated_N08_image05_sp` |

## HER_Tafel_explicit_water

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| N17 | neb | superseded | diagnostic | (not recorded) | `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2_explicit_water` |
| N18 | neb | provisional | supporting | Resolve the H-H bond-forming region of the N17 hydrated Tafel pathway. | `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2_explicit_water_refined16` |
| N19 | neb | provisional | core | Tafel recombination from independently optimized on-top surface H. | `kinetics/Pb111/fixed_mu/m0p1193/Tafel_ontop2H_to_H2_explicit_water` |
| X87 | go | validated | core | Validate hydrated Tafel HER endpoint before any new NEB. | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/hydrated_surface_2H` |
| X88 | go | validated | supporting | Validate hydrated Tafel HER endpoint before any new NEB. | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/hydrated_H2_product` |
| X90 | go | validated | core | Relax lower-energy, on-top-like surface-2H configuration. | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/relax_2H_from_N18_image05` |
| X91 | go | validated | supporting | Relax lower-energy, nearly vertical H2 product configuration. | `surfaces/Pb111/HER/Tafel/explicit_water/m0p1193/relax_H2_from_N18_image14` |

## NEB

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| N08 | neb | invalid | diagnostic | Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential. | `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2` |
| N09 | neb | invalid | diagnostic | Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential. | `kinetics/Pb111/fixed_mu/m0p11195/Tafel_surface2H_to_H2` |
| N10 | neb | invalid | diagnostic | Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential. | `kinetics/Pb111/fixed_mu/m0p1046/Tafel_surface2H_to_H2` |
| N11 | neb | invalid | diagnostic | Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential. | `kinetics/Pb111/fixed_mu/m0p09725/Tafel_surface2H_to_H2` |
| N12 | neb | superseded | diagnostic | Hydrated PbH2 extraction from a low-coordinate HCP Pb adatom at fixed electron chemical potential. | `kinetics/Pb111/fixed_mu/m0p1193/adatom_hcp_PbH2_to_detached_explicit_water` |
| N13 | neb | provisional | diagnostic | Hydrated PbH2 extraction from a low-coordinate FCC Pb adatom at fixed electron chemical potential. | `kinetics/Pb111/fixed_mu/m0p0899/adatom_fcc_PbH2_to_detached_explicit_water` |
| N14 | neb | provisional | core | Hydrated terrace PbH2 extraction at fixed electron chemical potential, providing the matched terrace control for the HCP-adatom extraction NEB N12. | `kinetics/Pb111/fixed_mu/m0p1193/terrace_PbH2_to_detached_explicit_water` |
| N15 | neb | invalid | diagnostic | Hydrated terrace PbH2 extraction at fixed electron chemical potential, providing the matched terrace control for the FCC-adatom extraction NEB N13. | `kinetics/Pb111/fixed_mu/m0p0899/terrace_PbH2_to_detached_explicit_water` |
| N16 | neb | provisional | core | Hydrated HCP-adatom PbH2 extraction from independently relaxed X86 to X44. | `kinetics/Pb111/fixed_mu/m0p1193/adatom_hcp_PbH2_X86_to_X44_explicit_water` |

## PbH2_extraction

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X01 | go | provisional | supporting | Neutral PbH2-extraction endpoint search with the Pb(H)2 moiety initially translated so its Pb atom is 2.5 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_2p5` |
| X02 | go | provisional | supporting | Neutral PbH2-extraction endpoint search with the Pb(H)2 moiety initially translated so its Pb atom is 4.0 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_4p0` |
| X03 | go | provisional | supporting | Neutral PbH2-extraction endpoint search with the Pb(H)2 moiety initially translated so its Pb atom is 6.0 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_6p0` |
| X04 | go | provisional | diagnostic | Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 2.5 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_2p5` |
| X05 | go | provisional | diagnostic | Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 4.0 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_4p0` |
| X06 | go | provisional | supporting | Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 6.0 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_6p0` |

## PbH2_extraction_explicit_water

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X28 | go | validated | core | Construct a detached PbH2 + vacancy product with two hydride-oriented explicit first-shell water molecules so that PbH2 detachment can be compared against the hydrated surface Pb(H)2 precursor at identical stoichiometry and target-mu. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p1193` |
| X29 | go | validated | supporting | Construct a detached PbH2 + vacancy product with two hydride-oriented explicit first-shell water molecules so that PbH2 detachment can be compared against the hydrated surface Pb(H)2 precursor at identical stoichiometry and target-mu. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p09725` |
| X30 | go | validated | supporting | Continue the physical hydrated detached PbH2 branch to complete the fixed-mu detachment curve. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p11195` |
| X31 | go | validated | supporting | Continue the physical hydrated detached PbH2 branch to complete the fixed-mu detachment curve. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p1046` |
| X32 | go | validated | supporting | Continue the physical hydrated detached PbH2 branch to complete the fixed-mu detachment curve. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p0899` |

## PbH2_formation_explicit_water

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X92 | go | provisional | core | Test whether a terrace Pb(H)2-like precursor is a local minimum in the hydration environment of the independently optimized on-top two-H reactant X90. | `surfaces/Pb111/PbH2_formation/explicit_water/m0p1193/relax_X21_hydride_with_X90_water` |

## PbH2_potential_sweep

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X08 | go | provisional | diagnostic | Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor. | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p11195` |
| X09 | go | provisional | diagnostic | Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor. | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p1046` |
| X10 | go | provisional | diagnostic | Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor. | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p09725` |
| X11 | go | provisional | supporting | Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor. | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p0899` |
| X12 | go | provisional | diagnostic | Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy. | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p11195` |
| X13 | go | provisional | diagnostic | Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy. | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p1046` |
| X14 | go | provisional | diagnostic | Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy. | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p09725` |
| X15 | go | provisional | diagnostic | Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy. | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p0899` |
| X16 | go | provisional | supporting | Separation-convergence check for detached PbH2 at target-mu = -0.1193 Ha; the intact PbH2 unit from X06 is translated 1.5 Å farther from the Pb(111) surface. | `surfaces/Pb111/PbH2_extraction/separation/fixed_mu/m0p1193/plus_1p5` |

## adatom_PbH2_explicit_water

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X33 | go | superseded | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p1193` |
| X34 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p1193` |
| X35 | go | superseded | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p11195` |
| X36 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p11195` |
| X37 | go | superseded | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p1046` |
| X38 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p1046` |
| X39 | go | superseded | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p09725` |
| X40 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p09725` |
| X41 | go | provisional | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p0899` |
| X42 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p0899` |
| X43 | go | superseded | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p1193` |
| X44 | go | provisional | core | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p1193` |
| X45 | go | superseded | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p11195` |
| X46 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p11195` |
| X47 | go | superseded | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p1046` |
| X48 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p1046` |
| X49 | go | superseded | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p09725` |
| X50 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p09725` |
| X51 | go | provisional | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p0899` |
| X52 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p0899` |
| X78 | go | provisional | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p1193` |
| X79 | go | provisional | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p11195` |
| X80 | go | provisional | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p1046` |
| X81 | go | provisional | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p09725` |
| X82 | go | provisional | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p11195` |
| X83 | go | provisional | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p1046` |
| X84 | go | provisional | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p09725` |
| X85 | go | provisional | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p0899` |
| X86 | go | validated | supporting | Independently relax N12 NEB image 01 to determine whether its 0.157 eV stabilization represents a physical lower-energy precursor. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_from_N12_image01/m0p1193` |

## bulk_reference

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| B01 | bulk_reference | provisional | core | Optimize the bulk FCC Pb lattice constant used to construct all Pb surface models. | `bulk/Pb_fcc` |

## clean

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| S01 | go | provisional | core | Primary clean Pb(111) parent: 4 layers, 4x4x1 k-point mesh. | `surfaces/Pb111/clean` |

## convergence

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| S02 | go | provisional | supporting | Clean Pb(111), 4 layers, denser 6x6x1 k-point sampling. | `surfaces/Pb111/convergence/4L_k6` |
| S03 | go | provisional | supporting | Clean Pb(111), 5 layers, slab-thickness comparison. | `surfaces/Pb111/convergence/5L_k4` |
| S04 | go | provisional | supporting | Clean Pb(111), 6 layers, slab-thickness comparison. | `surfaces/Pb111/convergence/6L_k4` |

## defect

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| D01 | go | provisional | supporting | Pb(111) with one top-layer Pb vacancy; corrosion/extraction endpoint reference. | `surfaces/Pb111/defects/vacancy` |
| D02 | go | provisional | supporting | Pb adatom initially placed at the Pb(111) fcc hollow. | `surfaces/Pb111/defects/adatom_fcc` |
| D03 | go | provisional | supporting | Pb adatom initially placed at the Pb(111) hcp hollow. | `surfaces/Pb111/defects/adatom_hcp` |

## fixed_mu_1H

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| MH01 | go | provisional | supporting | One-H Pb(111) ontop geometry relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p1193` |
| MH02 | go | provisional | diagnostic | One-H Pb(111) ontop geometry relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p1046` |
| MH03 | go | provisional | diagnostic | One-H Pb(111) ontop geometry relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p0899` |
| MH04 | go | provisional | supporting | One-H Pb(111) bridge geometry relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p1193` |
| MH05 | go | provisional | diagnostic | One-H Pb(111) bridge geometry relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p1046` |
| MH06 | go | provisional | diagnostic | One-H Pb(111) bridge geometry relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p0899` |
| MH07 | go | provisional | supporting | One-H Pb(111) fcc geometry relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p1193` |
| MH08 | go | provisional | diagnostic | One-H Pb(111) fcc geometry relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p1046` |
| MH09 | go | provisional | diagnostic | One-H Pb(111) fcc geometry relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p0899` |
| MH10 | go | provisional | supporting | One-H Pb(111) hcp geometry relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p1193` |
| MH11 | go | provisional | diagnostic | One-H Pb(111) hcp geometry relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p1046` |
| MH12 | go | provisional | diagnostic | One-H Pb(111) hcp geometry relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p0899` |

## fixed_mu_2H

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| M2H01 | go | provisional | core | Two-H candidate 'fcc_hcp' relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p1193` |
| M2H02 | go | provisional | diagnostic | Two-H candidate 'fcc_hcp' relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p1046` |
| M2H03 | go | provisional | supporting | Two-H candidate 'fcc_hcp' relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p0899` |
| M2H04 | go | provisional | core | Two-H candidate 'shared_bridges' relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p1193` |
| M2H05 | go | provisional | diagnostic | Two-H candidate 'shared_bridges' relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p1046` |
| M2H06 | go | provisional | supporting | Two-H candidate 'shared_bridges' relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p0899` |
| M2H07 | go | provisional | core | Two-H candidate 'PbH2_like' relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p1193` |
| M2H08 | go | provisional | diagnostic | Two-H candidate 'PbH2_like' relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p1046` |
| M2H09 | go | provisional | supporting | Two-H candidate 'PbH2_like' relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p0899` |
| X17 | go | provisional | diagnostic | Test whether the separated two-H surface basin remains a physical local minimum at target-mu = -0.11195 Ha. | `surfaces/Pb111/fixed_mu/H2_reference/separated/m0p11195` |
| X18 | go | provisional | diagnostic | Test whether the same-Pb two-H surface basin remains a physical local minimum at target-mu = -0.11195 Ha. | `surfaces/Pb111/fixed_mu/H2_reference/same_Pb/m0p11195` |
| X19 | go | provisional | supporting | Continue a chemically valid separated two-H surface state to target-mu = -0.09725 Ha. | `surfaces/Pb111/fixed_mu/H2_reference/separated/m0p09725` |
| X20 | go | provisional | supporting | Test whether the same-Pb two-H surface basin survives at target-mu = -0.09725 Ha. | `surfaces/Pb111/fixed_mu/H2_reference/same_Pb/m0p09725` |

## fixed_mu_H2_endpoint

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X53 | go | provisional | supporting | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1193/z4p0` |
| X54 | go | provisional | supporting | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1193/z6p0` |
| X55 | go | provisional | supporting | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p11195/z4p0` |
| X56 | go | provisional | supporting | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p11195/z6p0` |
| X57 | go | provisional | supporting | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1046/z4p0` |
| X58 | go | provisional | supporting | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1046/z6p0` |
| X59 | go | provisional | supporting | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p09725/z4p0` |
| X60 | go | provisional | supporting | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p09725/z6p0` |

## fixed_mu_clean

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| G01 | go | provisional | core | Clean Pb(111) relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/clean/m0p1193` |
| G02 | go | provisional | core | Clean Pb(111) relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/clean/m0p1046` |
| G03 | go | provisional | core | Clean Pb(111) relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/clean/m0p0899` |
| X61 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/clean/m0p11195` |
| X62 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/clean/m0p09725` |

## fixed_mu_defect

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X63 | go | provisional | core | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p1193` |
| X64 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p11195` |
| X65 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p1046` |
| X66 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p09725` |
| X67 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p0899` |
| X68 | go | provisional | core | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p1193` |
| X69 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p11195` |
| X70 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p1046` |
| X71 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p09725` |
| X72 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p0899` |
| X73 | go | provisional | core | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p1193` |
| X74 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p11195` |
| X75 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p1046` |
| X76 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p09725` |
| X77 | go | provisional | supporting | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p0899` |

## fixed_mu_neb

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| N01 | neb | provisional | supporting | Grand-canonical NEB from ordinary surface-bound H to the lifted Pb-H state at target-mu = -0.1193 Ha. | `kinetics/Pb111/fixed_mu/m0p1193/surface_H_to_lifted_PbH` |
| N02 | neb | provisional | supporting | Grand-canonical NEB from two H atoms associated with different Pb atoms to the same-Pb Pb(H)2 surface state at target-mu = -0.1193 Ha. | `kinetics/Pb111/fixed_mu/m0p1193/separated_2H_to_same_Pb` |
| N03 | neb | provisional | supporting | Grand-canonical NEB from the mildly lifted same-Pb Pb(H)2 surface state to the strongly lifted incipient-extraction state at target-mu = -0.1193 Ha. | `kinetics/Pb111/fixed_mu/m0p1193/PbH2_surface_to_strongly_lifted` |
| N07 | neb | provisional | supporting | Fixed-mu first-stage NEB from strongly lifted surface Pb(H)2 to asymptotically detached PbH2 plus a Pb vacancy. | `kinetics/Pb111/fixed_mu/m0p1193/PbH2_strongly_lifted_to_detached` |

## neutral_1H

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| H01 | go | provisional | supporting | One H initially adsorbed at the Pb(111) ontop site. | `surfaces/Pb111/H_adsorption/ontop` |
| H02 | go | provisional | supporting | One H initially adsorbed at the Pb(111) bridge site. | `surfaces/Pb111/H_adsorption/bridge` |
| H03 | go | provisional | supporting | One H initially adsorbed at the Pb(111) fcc site. | `surfaces/Pb111/H_adsorption/fcc` |
| H04 | go | provisional | supporting | One H initially adsorbed at the Pb(111) hcp site. | `surfaces/Pb111/H_adsorption/hcp` |

## neutral_2H

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| HH01 | go | provisional | supporting | Two surface H atoms initially occupying neighboring FCC and HCP hollow environments. | `surfaces/Pb111/H2_candidates/fcc_hcp` |
| HH02 | go | provisional | core | Two H atoms initially placed at two bridge sites sharing the same top-layer Pb atom. | `surfaces/Pb111/H2_candidates/shared_bridges` |
| HH03 | go | provisional | core | Two H atoms initially arranged as a bent PbH2-like moiety on one top-layer Pb atom; Pb-H = 1.90 Å initial guess. | `surfaces/Pb111/H2_candidates/PbH2_like` |

## neutral_neb

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| N04 | neb | provisional | low | Neutral NEB from the lowest ordinary surface-H state to the deep subsurface-H / Pb-lifted minimum. | `kinetics/Pb111/neutral/surface_H_to_deep_subsurface_H` |
| N05 | neb | provisional | supporting | Neutral first-stage NEB from same-Pb surface Pb(H)2 to the partially extracted Pb(H)2 minimum. | `kinetics/Pb111/neutral/PbH2_surface_to_partially_extracted` |
| N06 | neb | provisional | supporting | Neutral first-stage NEB from partially extracted Pb(H)2 to detached PbH2 above a Pb vacancy. | `kinetics/Pb111/neutral/PbH2_partially_extracted_to_detached` |

## proton_well_rescue

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X21 | go | provisional | core | Test whether two explicit first-shell water molecules prevent the CANDLE proton-well artifact for strongly lifted surface Pb(H)2 at fixed electron chemical potential. | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p1193` |
| X22 | go | provisional | supporting | Test whether two explicit first-shell water molecules prevent the CANDLE proton-well artifact for strongly lifted surface Pb(H)2 at fixed electron chemical potential. | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p09725` |
| X23 | go | provisional | diagnostic | Test whether two explicit first-shell water molecules prevent the CANDLE proton-well artifact for strongly lifted surface Pb(H)2 at fixed electron chemical potential. | `surfaces/Pb111/proton_well_rescue/proton_oriented/m0p1193` |
| X24 | go | provisional | diagnostic | Test whether two explicit first-shell water molecules prevent the CANDLE proton-well artifact for strongly lifted surface Pb(H)2 at fixed electron chemical potential. | `surfaces/Pb111/proton_well_rescue/proton_oriented/m0p09725` |
| X25 | go | provisional | supporting | Continue the successful hydride-oriented explicit-water Pb(H)2 branch across fixed electron chemical potential to test whether first-shell water suppresses the CANDLE proton-well artifact. | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p11195` |
| X26 | go | provisional | supporting | Continue the successful hydride-oriented explicit-water Pb(H)2 branch across fixed electron chemical potential to test whether first-shell water suppresses the CANDLE proton-well artifact. | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p1046` |
| X27 | go | provisional | supporting | Continue the successful hydride-oriented explicit-water Pb(H)2 branch across fixed electron chemical potential to test whether first-shell water suppresses the CANDLE proton-well artifact. | `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p0899` |

## subsurface_H

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| SH01 | go | provisional | supporting | One H initially placed halfway between the first and second Pb layers, laterally registered with the fcc surface site. | `surfaces/Pb111/H_subsurface/fcc` |
| SH02 | go | provisional | supporting | One H initially placed halfway between the first and second Pb layers, laterally registered with the hcp surface site. | `surfaces/Pb111/H_subsurface/hcp` |
| SH03 | go | provisional | supporting | One H initially placed halfway between the first and second Pb layers, laterally registered with the ontop surface site. | `surfaces/Pb111/H_subsurface/ontop` |
| X07 | go | provisional | diagnostic | Test whether the deep subsurface-H / Pb-lifted structure remains a local minimum at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_subsurface/deep/m0p1193` |

## Scientific notes

### B01

**Location:** `bulk/Pb_fcc`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Optimize the bulk FCC Pb lattice constant used to construct all Pb surface models.

**Assessment:** Bulk face-centered-cubic Pb reference used to construct the slabs. The ledger records F = -243.951102 Ha and initial lattice parameter 5.0 A; child slab metadata reference an optimized lattice parameter near 4.974795 A. The optimizer log and Slurm provenance are not recovered for this bulk entry.

**Caveats:** Verify the final bulk cell and convergence settings from the raw output before documenting the reference lattice constant.

### D01

**Location:** `surfaces/Pb111/defects/vacancy`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Pb(111) with one top-layer Pb vacancy; corrosion/extraction endpoint reference.

**Assessment:** Neutral Pb(111) top-layer vacancy reference, used to initialize the defect and hydride extraction studies. Final reported fmax 0.0376 eV/A after 18 FIRE steps; scheduler: COMPLETED. It supplies geometries, not a standalone grand-canonical defect formation energy.

**Caveats:** Compute balanced vacancy/adatom formation cycles using matched clean surfaces and identical electron chemical potential for meaningful defect costs.

### D02

**Location:** `surfaces/Pb111/defects/adatom_fcc`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Pb adatom initially placed at the Pb(111) fcc hollow.

**Assessment:** Neutral Pb(111) FCC Pb adatom reference, used to initialize the defect and hydride extraction studies. Final reported fmax 0.0198 eV/A after 34 FIRE steps; scheduler: COMPLETED. It supplies geometries, not a standalone grand-canonical defect formation energy.

**Caveats:** Compute balanced vacancy/adatom formation cycles using matched clean surfaces and identical electron chemical potential for meaningful defect costs.

### D03

**Location:** `surfaces/Pb111/defects/adatom_hcp`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Pb adatom initially placed at the Pb(111) hcp hollow.

**Assessment:** Neutral Pb(111) HCP Pb adatom reference, used to initialize the defect and hydride extraction studies. Final reported fmax 0.0391 eV/A after 36 FIRE steps; scheduler: COMPLETED. It supplies geometries, not a standalone grand-canonical defect formation energy.

**Caveats:** Compute balanced vacancy/adatom formation cycles using matched clean surfaces and identical electron chemical potential for meaningful defect costs.

### G01

**Location:** `surfaces/Pb111/fixed_mu/clean/m0p1193`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Clean Pb(111) relaxed at target-mu = -0.1193 Ha.

**Assessment:** Fixed-electron-chemical-potential clean Pb(111) slab reference at target mu=-0.11930 Ha; G=-2135.241860209 Ha. Final reported fmax 0.0360 eV/A after 13 FIRE steps; scheduler: COMPLETED. Provides clean-surface grand potential for matched adsorbate/defect cycles.

**Caveats:** Reference calculations have different equilibrium electron counts at different mu; G values at different potentials are not direct reaction energies.

### G02

**Location:** `surfaces/Pb111/fixed_mu/clean/m0p1046`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Clean Pb(111) relaxed at target-mu = -0.1046 Ha.

**Assessment:** Fixed-electron-chemical-potential clean Pb(111) slab reference at target mu=-0.10460 Ha; G=-2142.679120948 Ha. Final reported fmax 0.0260 eV/A after 7 FIRE steps; scheduler: COMPLETED. Provides clean-surface grand potential for matched adsorbate/defect cycles.

**Caveats:** Reference calculations have different equilibrium electron counts at different mu; G values at different potentials are not direct reaction energies.

### G03

**Location:** `surfaces/Pb111/fixed_mu/clean/m0p0899`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Clean Pb(111) relaxed at target-mu = -0.0899 Ha.

**Assessment:** Fixed-electron-chemical-potential clean Pb(111) slab reference at target mu=-0.08990 Ha; G=-2150.132763361 Ha. Final reported fmax 0.0240 eV/A after 17 FIRE steps; scheduler: COMPLETED. Provides clean-surface grand potential for matched adsorbate/defect cycles.

**Caveats:** Reference calculations have different equilibrium electron counts at different mu; G values at different potentials are not direct reaction energies.

### H01

**Location:** `surfaces/Pb111/H_adsorption/ontop`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One H initially adsorbed at the Pb(111) ontop site.

**Assessment:** Neutral adsorption-screen geometry initialized as on-top single H. The final fixed-electron-number energy is +0.164 eV relative to the lowest-F member of this same-stoichiometry trial set (H03). Final reported fmax 0.0387 eV/A after 32 FIRE steps; scheduler: COMPLETED.

**Caveats:** Starting site labels do not establish final adsorption sites; verify relaxed structures and account for solvent/electronic model before claiming site ordering.

### H02

**Location:** `surfaces/Pb111/H_adsorption/bridge`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One H initially adsorbed at the Pb(111) bridge site.

**Assessment:** Neutral adsorption-screen geometry initialized as bridge single H. The final fixed-electron-number energy is +0.003 eV relative to the lowest-F member of this same-stoichiometry trial set (H03). Final reported fmax 0.0144 eV/A after 47 FIRE steps; scheduler: COMPLETED.

**Caveats:** Starting site labels do not establish final adsorption sites; verify relaxed structures and account for solvent/electronic model before claiming site ordering.

### H03

**Location:** `surfaces/Pb111/H_adsorption/fcc`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One H initially adsorbed at the Pb(111) fcc site.

**Assessment:** Neutral adsorption-screen geometry initialized as FCC-hollow single H. The final fixed-electron-number energy is +0.000 eV relative to the lowest-F member of this same-stoichiometry trial set (H03). Final reported fmax 0.0358 eV/A after 36 FIRE steps; scheduler: COMPLETED.

**Caveats:** Starting site labels do not establish final adsorption sites; verify relaxed structures and account for solvent/electronic model before claiming site ordering.

### H04

**Location:** `surfaces/Pb111/H_adsorption/hcp`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One H initially adsorbed at the Pb(111) hcp site.

**Assessment:** Neutral adsorption-screen geometry initialized as HCP-hollow single H. The final fixed-electron-number energy is +0.154 eV relative to the lowest-F member of this same-stoichiometry trial set (H03). Final reported fmax 0.0338 eV/A after 20 FIRE steps; scheduler: COMPLETED.

**Caveats:** Starting site labels do not establish final adsorption sites; verify relaxed structures and account for solvent/electronic model before claiming site ordering.

### HH01

**Location:** `surfaces/Pb111/H2_candidates/fcc_hcp`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Two surface H atoms initially occupying neighboring FCC and HCP hollow environments.

**Assessment:** Neutral adsorption-screen geometry initialized as FCC/HCP separated two-H. The final fixed-electron-number energy is +0.100 eV relative to the lowest-F member of this same-stoichiometry trial set (HH03). Final reported fmax 0.0317 eV/A after 36 FIRE steps; scheduler: COMPLETED.

**Caveats:** Starting site labels do not establish final adsorption sites; verify relaxed structures and account for solvent/electronic model before claiming site ordering.

### HH02

**Location:** `surfaces/Pb111/H2_candidates/shared_bridges`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Two H atoms initially placed at two bridge sites sharing the same top-layer Pb atom.

**Assessment:** Neutral adsorption-screen geometry initialized as shared-bridge two-H around one Pb. The final fixed-electron-number energy is +0.008 eV relative to the lowest-F member of this same-stoichiometry trial set (HH03). Final reported fmax 0.0327 eV/A after 35 FIRE steps; scheduler: COMPLETED.

**Caveats:** Starting site labels do not establish final adsorption sites; verify relaxed structures and account for solvent/electronic model before claiming site ordering.

### HH03

**Location:** `surfaces/Pb111/H2_candidates/PbH2_like`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Two H atoms initially arranged as a bent PbH2-like moiety on one top-layer Pb atom; Pb-H = 1.90 Å initial guess.

**Assessment:** Neutral adsorption-screen geometry initialized as initial bent PbH2-like two-H. The final fixed-electron-number energy is +0.000 eV relative to the lowest-F member of this same-stoichiometry trial set (HH03). Final reported fmax 0.0387 eV/A after 65 FIRE steps; scheduler: COMPLETED.

**Caveats:** Starting site labels do not establish final adsorption sites; verify relaxed structures and account for solvent/electronic model before claiming site ordering.

### M2H01

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p1193`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Two-H candidate 'fcc_hcp' relaxed at target-mu = -0.1193 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as fcc_hcp, at target mu=-0.11930 Ha. G=-2136.117244903 Ha, +0.112 eV relative to lowest two-H numerical value for this mu (M2H07); Final reported fmax 0.0356 eV/A after 34 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units.

**Caveats:** Same-mu energy comparison is preliminary; the starting site name may not identify the relaxed minimum and dry-model results do not substitute for hydrated calculations.

### M2H02

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Two-H candidate 'fcc_hcp' relaxed at target-mu = -0.1046 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as fcc_hcp, at target mu=-0.10460 Ha. G=-2143.860734050 Ha, +7.709 eV relative to lowest two-H numerical value for this mu (M2H08); Final reported fmax 0.0397 eV/A after 91 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units. Multi-eV separation among nominally comparable two-H surfaces is suspicious; do not interpret it as a normal adsorption-site preference.

**Caveats:** CRITICAL: cross-check electronic population, cavity construction, and final state before including this G difference in a thermodynamic comparison.

### M2H03

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Two-H candidate 'fcc_hcp' relaxed at target-mu = -0.0899 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as fcc_hcp, at target mu=-0.08990 Ha. G=-2151.594765858 Ha, +0.012 eV relative to lowest two-H numerical value for this mu (M2H09); Final reported fmax 0.0230 eV/A after 93 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units.

**Caveats:** Same-mu energy comparison is preliminary; the starting site name may not identify the relaxed minimum and dry-model results do not substitute for hydrated calculations.

### M2H04

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p1193`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Two-H candidate 'shared_bridges' relaxed at target-mu = -0.1193 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as shared_bridges, at target mu=-0.11930 Ha. G=-2136.120146382 Ha, +0.034 eV relative to lowest two-H numerical value for this mu (M2H07); Final reported fmax 0.0388 eV/A after 32 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units.

**Caveats:** Same-mu energy comparison is preliminary; the starting site name may not identify the relaxed minimum and dry-model results do not substitute for hydrated calculations.

### M2H05

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Two-H candidate 'shared_bridges' relaxed at target-mu = -0.1046 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as shared_bridges, at target mu=-0.10460 Ha. G=-2143.585300072 Ha, +15.203 eV relative to lowest two-H numerical value for this mu (M2H08); Final reported fmax 0.0367 eV/A after 31 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units. Multi-eV separation among nominally comparable two-H surfaces is suspicious; do not interpret it as a normal adsorption-site preference.

**Caveats:** CRITICAL: cross-check electronic population, cavity construction, and final state before including this G difference in a thermodynamic comparison.

### M2H06

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Two-H candidate 'shared_bridges' relaxed at target-mu = -0.0899 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as shared_bridges, at target mu=-0.08990 Ha. G=-2151.594825256 Ha, +0.010 eV relative to lowest two-H numerical value for this mu (M2H09); Final reported fmax 0.0384 eV/A after 88 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units.

**Caveats:** Same-mu energy comparison is preliminary; the starting site name may not identify the relaxed minimum and dry-model results do not substitute for hydrated calculations.

### M2H07

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p1193`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Two-H candidate 'PbH2_like' relaxed at target-mu = -0.1193 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as PbH2_like, at target mu=-0.11930 Ha. G=-2136.121378243 Ha, +0.000 eV relative to lowest two-H numerical value for this mu (M2H07); Final reported fmax 0.0318 eV/A after 62 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units.

**Caveats:** Same-mu energy comparison is preliminary; the starting site name may not identify the relaxed minimum and dry-model results do not substitute for hydrated calculations.

### M2H08

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Two-H candidate 'PbH2_like' relaxed at target-mu = -0.1046 Ha.

**Assessment:** Earlier dry/fixed-potential PbH2-like surface GO at -1.4 V RHE timed out with maximum force 0.057769 eV/A.

**Caveats:** Not converged to the 0.04 eV/A GO criterion; not independently reviewed structurally.

### M2H09

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Two-H candidate 'PbH2_like' relaxed at target-mu = -0.0899 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as PbH2_like, at target mu=-0.08990 Ha. G=-2151.595197178 Ha, +0.000 eV relative to lowest two-H numerical value for this mu (M2H09); Final reported fmax 0.0330 eV/A after 74 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units.

**Caveats:** Same-mu energy comparison is preliminary; the starting site name may not identify the relaxed minimum and dry-model results do not substitute for hydrated calculations.

### MH01

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p1193`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One-H Pb(111) ontop geometry relaxed at target-mu = -0.1193 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in ontop environment (target mu=-0.11930 Ha). G=-2135.683838682 Ha, +0.000 eV relative to the smallest extracted G for this mu (MH01). Final reported fmax 0.0358 eV/A after 34 FIRE steps; scheduler: COMPLETED.

**Caveats:** Relative G is a same-mu numerical contrast only; validate atomic geometry, electron branch, and solvation before claiming the preferred site.

### MH02

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** One-H Pb(111) ontop geometry relaxed at target-mu = -0.1046 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in ontop environment (target mu=-0.10460 Ha). G=-2143.407087255 Ha, +0.000 eV relative to the smallest extracted G for this mu (MH02). Final reported fmax 0.0227 eV/A after 26 FIRE steps; scheduler: COMPLETED. The multi-eV separation between nominally same-stoichiometry surface-H trials is anomalously large for an adsorption-site difference and suggests an electronic, cavity, or structural-state inconsistency.

**Caveats:** CRITICAL: do not use these computed site energy differences as adsorption thermodynamics until final geometries, charge, and solvation-cavity branches are checked.

### MH03

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p0899`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** One-H Pb(111) ontop geometry relaxed at target-mu = -0.0899 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in ontop environment (target mu=-0.08990 Ha). G=-2150.863320844 Ha, +0.023 eV relative to the smallest extracted G for this mu (MH12). Final reported fmax 0.0397 eV/A after 31 FIRE steps; scheduler: COMPLETED. The multi-eV separation between nominally same-stoichiometry surface-H trials is anomalously large for an adsorption-site difference and suggests an electronic, cavity, or structural-state inconsistency.

**Caveats:** CRITICAL: do not use these computed site energy differences as adsorption thermodynamics until final geometries, charge, and solvation-cavity branches are checked.

### MH04

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p1193`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One-H Pb(111) bridge geometry relaxed at target-mu = -0.1193 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in bridge environment (target mu=-0.11930 Ha). G=-2135.681716744 Ha, +0.058 eV relative to the smallest extracted G for this mu (MH01). Final reported fmax 0.0307 eV/A after 94 FIRE steps; scheduler: COMPLETED.

**Caveats:** Relative G is a same-mu numerical contrast only; validate atomic geometry, electron branch, and solvation before claiming the preferred site.

### MH05

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** One-H Pb(111) bridge geometry relaxed at target-mu = -0.1046 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in bridge environment (target mu=-0.10460 Ha). G=-2143.131405159 Ha, +7.502 eV relative to the smallest extracted G for this mu (MH02). Final reported fmax 0.0363 eV/A after 46 FIRE steps; scheduler: COMPLETED. The multi-eV separation between nominally same-stoichiometry surface-H trials is anomalously large for an adsorption-site difference and suggests an electronic, cavity, or structural-state inconsistency.

**Caveats:** CRITICAL: do not use these computed site energy differences as adsorption thermodynamics until final geometries, charge, and solvation-cavity branches are checked.

### MH06

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p0899`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** One-H Pb(111) bridge geometry relaxed at target-mu = -0.0899 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in bridge environment (target mu=-0.08990 Ha). G=-2150.863995553 Ha, +0.004 eV relative to the smallest extracted G for this mu (MH12). Final reported fmax 0.0288 eV/A after 58 FIRE steps; scheduler: COMPLETED. The multi-eV separation between nominally same-stoichiometry surface-H trials is anomalously large for an adsorption-site difference and suggests an electronic, cavity, or structural-state inconsistency.

**Caveats:** CRITICAL: do not use these computed site energy differences as adsorption thermodynamics until final geometries, charge, and solvation-cavity branches are checked.

### MH07

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p1193`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One-H Pb(111) fcc geometry relaxed at target-mu = -0.1193 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in fcc environment (target mu=-0.11930 Ha). G=-2135.681905207 Ha, +0.053 eV relative to the smallest extracted G for this mu (MH01). Final reported fmax 0.0354 eV/A after 31 FIRE steps; scheduler: COMPLETED.

**Caveats:** Relative G is a same-mu numerical contrast only; validate atomic geometry, electron branch, and solvation before claiming the preferred site.

### MH08

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** One-H Pb(111) fcc geometry relaxed at target-mu = -0.1046 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in fcc environment (target mu=-0.10460 Ha). G=-2143.132191224 Ha, +7.480 eV relative to the smallest extracted G for this mu (MH02). Final reported fmax 0.0261 eV/A after 31 FIRE steps; scheduler: COMPLETED. The multi-eV separation between nominally same-stoichiometry surface-H trials is anomalously large for an adsorption-site difference and suggests an electronic, cavity, or structural-state inconsistency.

**Caveats:** CRITICAL: do not use these computed site energy differences as adsorption thermodynamics until final geometries, charge, and solvation-cavity branches are checked.

### MH09

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p0899`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** One-H Pb(111) fcc geometry relaxed at target-mu = -0.0899 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in fcc environment (target mu=-0.08990 Ha). G=-2150.599190941 Ha, +7.210 eV relative to the smallest extracted G for this mu (MH12). Final reported fmax 0.0329 eV/A after 27 FIRE steps; scheduler: COMPLETED. The multi-eV separation between nominally same-stoichiometry surface-H trials is anomalously large for an adsorption-site difference and suggests an electronic, cavity, or structural-state inconsistency.

**Caveats:** CRITICAL: do not use these computed site energy differences as adsorption thermodynamics until final geometries, charge, and solvation-cavity branches are checked.

### MH10

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p1193`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One-H Pb(111) hcp geometry relaxed at target-mu = -0.1193 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in hcp environment (target mu=-0.11930 Ha). G=-2135.677373029 Ha, +0.176 eV relative to the smallest extracted G for this mu (MH01). Final reported fmax 0.0395 eV/A after 20 FIRE steps; scheduler: COMPLETED.

**Caveats:** Relative G is a same-mu numerical contrast only; validate atomic geometry, electron branch, and solvation before claiming the preferred site.

### MH11

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** One-H Pb(111) hcp geometry relaxed at target-mu = -0.1046 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in hcp environment (target mu=-0.10460 Ha). G=-2143.129462913 Ha, +7.555 eV relative to the smallest extracted G for this mu (MH02). Final reported fmax 0.0346 eV/A after 29 FIRE steps; scheduler: COMPLETED. The multi-eV separation between nominally same-stoichiometry surface-H trials is anomalously large for an adsorption-site difference and suggests an electronic, cavity, or structural-state inconsistency.

**Caveats:** CRITICAL: do not use these computed site energy differences as adsorption thermodynamics until final geometries, charge, and solvation-cavity branches are checked.

### MH12

**Location:** `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p0899`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** One-H Pb(111) hcp geometry relaxed at target-mu = -0.0899 Ha.

**Assessment:** One-H fixed-potential adsorption trial initialized in hcp environment (target mu=-0.08990 Ha). G=-2150.864153511 Ha, +0.000 eV relative to the smallest extracted G for this mu (MH12). Final reported fmax 0.0316 eV/A after 61 FIRE steps; scheduler: COMPLETED. The multi-eV separation between nominally same-stoichiometry surface-H trials is anomalously large for an adsorption-site difference and suggests an electronic, cavity, or structural-state inconsistency.

**Caveats:** CRITICAL: do not use these computed site energy differences as adsorption thermodynamics until final geometries, charge, and solvation-cavity branches are checked.

### N01

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/surface_H_to_lifted_PbH`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Grand-canonical NEB from ordinary surface-bound H to the lifted Pb-H state at target-mu = -0.1193 Ha.

**Assessment:** Early continuum-only fixed-potential migration of one adsorbed H from FCC-like to lifted on-top Pb-H configuration. Sampled maximum +0.149078 eV and endpoint difference -0.052613 eV; converged nonclimbing NEB at 0.061821 eV/A.

**Caveats:** Approximate pathway screen only; inspect actual geometry before assigning a single-H mechanistic label or rate constant.

**Extracted sampled maximum:** +0.149078 eV; **endpoint difference:** -0.052613 eV (G).

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

### N04

**Location:** `kinetics/Pb111/neutral/surface_H_to_deep_subsurface_H`. **Priority:** low. **Review state:** provisional.

**Setup intent:** Neutral NEB from the lowest ordinary surface-H state to the deep subsurface-H / Pb-lifted minimum.

**Assessment:** Neutral H transfer from surface FCC environment to deep subsurface/Pb-lifted structure: sampled +0.290299 eV maximum and +0.048945 eV endpoint difference; NEB reached 0.070113 eV/A.

**Caveats:** Neutral electronic ensemble; not a fixed-potential Volmer step. Transition state and final geometry not independently verified.

**Extracted sampled maximum:** +0.290299 eV; **endpoint difference:** +0.048945 eV (F).

### N05

**Location:** `kinetics/Pb111/neutral/PbH2_surface_to_partially_extracted`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Neutral first-stage NEB from same-Pb surface Pb(H)2 to the partially extracted Pb(H)2 minimum.

**Assessment:** Neutral same-Pb surface Pb(H)2 to partially extracted Pb(H)2 screening NEB. Monotonically uphill within sampled band; +0.432827 eV endpoint energy difference, fmax 0.069064 eV/A.

**Caveats:** Continuum-only neutral model. Endpoint value is not an independently identified saddle-point barrier.

**Extracted sampled maximum:** +0.432827 eV; **endpoint difference:** +0.432827 eV (F).

### N06

**Location:** `kinetics/Pb111/neutral/PbH2_partially_extracted_to_detached`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Neutral first-stage NEB from partially extracted Pb(H)2 to detached PbH2 above a Pb vacancy.

**Assessment:** Neutral partially extracted to detached PbH2 screening NEB: sampled monotonically uphill, +0.819229 eV endpoint energy difference, fmax 0.076599 eV/A.

**Caveats:** Continuum-only neutral model; distinguish this segment from the full surface-to-detached transformation.

**Extracted sampled maximum:** +0.819229 eV; **endpoint difference:** +0.819229 eV (F).

### N07

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/PbH2_strongly_lifted_to_detached`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Fixed-mu first-stage NEB from strongly lifted surface Pb(H)2 to asymptotically detached PbH2 plus a Pb vacancy.

**Assessment:** Earlier fixed-potential strongly lifted surface Pb(H)2 to detached PbH2 pathway; sampled maximum +1.210523 eV, endpoint difference +1.207361 eV, fmax 0.071037 eV/A.

**Caveats:** Continuum-only earlier model. Do not substitute for validated explicit-water terrace detachment; image 08 slightly exceeds the endpoint.

**Extracted sampled maximum:** +1.210523 eV; **endpoint difference:** +1.207361 eV (G).

### N08

**Location:** `kinetics/Pb111/fixed_mu/m0p1193/Tafel_surface2H_to_H2`. **Priority:** diagnostic. **Review state:** invalid.

**Setup intent:** Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential.

**Assessment:** Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum (INVALID PATH; NOT A PHYSICAL BARRIER):** +0.047877 eV; **endpoint difference:** -1.311886 eV (G).

### N09

**Location:** `kinetics/Pb111/fixed_mu/m0p11195/Tafel_surface2H_to_H2`. **Priority:** diagnostic. **Review state:** invalid.

**Setup intent:** Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential.

**Assessment:** Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum (INVALID PATH; NOT A PHYSICAL BARRIER):** +0.057843 eV; **endpoint difference:** -1.314591 eV (G).

### N10

**Location:** `kinetics/Pb111/fixed_mu/m0p1046/Tafel_surface2H_to_H2`. **Priority:** diagnostic. **Review state:** invalid.

**Setup intent:** Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential.

**Assessment:** Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum (INVALID PATH; NOT A PHYSICAL BARRIER):** +0.027063 eV; **endpoint difference:** -1.341106 eV (G).

### N11

**Location:** `kinetics/Pb111/fixed_mu/m0p09725/Tafel_surface2H_to_H2`. **Priority:** diagnostic. **Review state:** invalid.

**Setup intent:** Tafel HER: two adsorbed H atoms to molecular H2 at fixed electron chemical potential.

**Assessment:** Dry Tafel NEB showed catastrophic artificial stabilization of separated hydrogen; not usable for activation kinetics.

**Caveats:** Retrospective from discussion; verify raw files before publication.

**Extracted sampled maximum (INVALID PATH; NOT A PHYSICAL BARRIER):** +0.000000 eV; **endpoint difference:** -1.381863 eV (G).

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

**Extracted sampled maximum (INVALID PATH; NOT A PHYSICAL BARRIER):** +1.554947 eV; **endpoint difference:** +1.554947 eV (G).

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

### S01

**Location:** `surfaces/Pb111/clean`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Primary clean Pb(111) parent: 4 layers, 4x4x1 k-point mesh.

**Assessment:** Four-layer clean Pb(111) slab baseline without applied electron chemical potential. Final reported fmax 0.0176 eV/A after 9 FIRE steps; scheduler: COMPLETED. This is the geometrical parent for subsequent surface chemistry, not itself an adsorption free energy.

**Caveats:** Verify slab-layer constraints and convergence tests; absolute slab energies cannot be compared to different atom counts.

### S02

**Location:** `surfaces/Pb111/convergence/4L_k6`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Clean Pb(111), 4 layers, denser 6x6x1 k-point sampling.

**Assessment:** Clean-slab numerical convergence control (denser 6x6x1 k-point mesh), compared conceptually with the four-layer 4x4x1 baseline. Final reported fmax 0.0382 eV/A after 9 FIRE steps; scheduler: COMPLETED. This is a component of numerical-method justification.

**Caveats:** Energies in different slab sizes require appropriate per-atom/per-surface normalizations; a convergence difference has not been reconstructed or verified here.

### S03

**Location:** `surfaces/Pb111/convergence/5L_k4`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Clean Pb(111), 5 layers, slab-thickness comparison.

**Assessment:** Clean-slab numerical convergence control (five-layer slab), compared conceptually with the four-layer 4x4x1 baseline. Final reported fmax 0.0323 eV/A after 20 FIRE steps; scheduler: COMPLETED. This is a component of numerical-method justification.

**Caveats:** Energies in different slab sizes require appropriate per-atom/per-surface normalizations; a convergence difference has not been reconstructed or verified here.

### S04

**Location:** `surfaces/Pb111/convergence/6L_k4`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Clean Pb(111), 6 layers, slab-thickness comparison.

**Assessment:** Clean-slab numerical convergence control (six-layer slab), compared conceptually with the four-layer 4x4x1 baseline. Final reported fmax 0.0397 eV/A after 8 FIRE steps; scheduler: COMPLETED. This is a component of numerical-method justification.

**Caveats:** Energies in different slab sizes require appropriate per-atom/per-surface normalizations; a convergence difference has not been reconstructed or verified here.

### SH01

**Location:** `surfaces/Pb111/H_subsurface/fcc`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One H initially placed halfway between the first and second Pb layers, laterally registered with the fcc surface site.

**Assessment:** Candidate subsurface-hydrogen / Pb-lifted configuration, initial designation H beneath top layer. neutral/fixed-electron-number calculation. Final reported fmax 0.0367 eV/A after 49 FIRE steps; scheduler: COMPLETED. Used to test whether hydrogen incorporation beneath the first Pb layer is competitive with surface adsorption.

**Caveats:** Verify whether H remains subsurface versus emerging to the surface; compare with matched one-H same-mu endpoints, not neutral values across ensembles.

### SH02

**Location:** `surfaces/Pb111/H_subsurface/hcp`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One H initially placed halfway between the first and second Pb layers, laterally registered with the hcp surface site.

**Assessment:** Candidate subsurface-hydrogen / Pb-lifted configuration, initial designation H beneath top layer. neutral/fixed-electron-number calculation. Final reported fmax 0.0346 eV/A after 35 FIRE steps; scheduler: COMPLETED. Used to test whether hydrogen incorporation beneath the first Pb layer is competitive with surface adsorption.

**Caveats:** Verify whether H remains subsurface versus emerging to the surface; compare with matched one-H same-mu endpoints, not neutral values across ensembles.

### SH03

**Location:** `surfaces/Pb111/H_subsurface/ontop`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** One H initially placed halfway between the first and second Pb layers, laterally registered with the ontop surface site.

**Assessment:** Candidate subsurface-hydrogen / Pb-lifted configuration, initial designation H beneath top layer. neutral/fixed-electron-number calculation. Final reported fmax 0.0310 eV/A after 29 FIRE steps; scheduler: COMPLETED. Used to test whether hydrogen incorporation beneath the first Pb layer is competitive with surface adsorption.

**Caveats:** Verify whether H remains subsurface versus emerging to the surface; compare with matched one-H same-mu endpoints, not neutral values across ensembles.

### X01

**Location:** `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_2p5`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Neutral PbH2-extraction endpoint search with the Pb(H)2 moiety initially translated so its Pb atom is 2.5 Å above the median Pb(111) surface plane.

**Assessment:** Initial PbH2 extraction endpoint search, initially displaced by 2p5 A, with neutral/fixed-electron-number calculation. Final reported fmax 0.0350 eV/A after 61 FIRE steps; scheduler: COMPLETED. Produced a geometry/energy endpoint for first-stage extraction comparisons.

**Caveats:** Neutral endpoint and geometry label require verification. Energies are not transferable directly into fixed-potential hydrated pathways.

### X02

**Location:** `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_4p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Neutral PbH2-extraction endpoint search with the Pb(H)2 moiety initially translated so its Pb atom is 4.0 Å above the median Pb(111) surface plane.

**Assessment:** Initial PbH2 extraction endpoint search, initially displaced by 4p0 A, with neutral/fixed-electron-number calculation. Final reported fmax 0.0353 eV/A after 116 FIRE steps; scheduler: COMPLETED. Produced a geometry/energy endpoint for first-stage extraction comparisons.

**Caveats:** Neutral endpoint and geometry label require verification. Energies are not transferable directly into fixed-potential hydrated pathways.

### X03

**Location:** `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_6p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Neutral PbH2-extraction endpoint search with the Pb(H)2 moiety initially translated so its Pb atom is 6.0 Å above the median Pb(111) surface plane.

**Assessment:** Initial PbH2 extraction endpoint search, initially displaced by 6p0 A, with neutral/fixed-electron-number calculation. Final reported fmax 0.0337 eV/A after 35 FIRE steps; scheduler: COMPLETED. Produced a geometry/energy endpoint for first-stage extraction comparisons.

**Caveats:** Neutral endpoint and geometry label require verification. Energies are not transferable directly into fixed-potential hydrated pathways.

### X04

**Location:** `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_2p5`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 2.5 Å above the median Pb(111) surface plane.

**Assessment:** Initial PbH2 extraction endpoint search, initially displaced by 2p5 A, with target mu=-0.11930 Ha. Final reported fmax 0.0328 eV/A after 75 FIRE steps; scheduler: COMPLETED. Produced a geometry/energy endpoint for first-stage extraction comparisons. The reported grand potential is about -16.177 eV relative to its putative same-stoichiometry source, an extreme stabilization inconsistent with a straightforward PbH2 lift.

**Caveats:** HIGH RISK: inspect hydrogen positions, electronic state, and continuum cavity; do not use this energy as a normal detachment minimum without further checks.

### X05

**Location:** `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_4p0`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 4.0 Å above the median Pb(111) surface plane.

**Assessment:** Early fixed-potential PbH2 extraction endpoint trial (4.0 A lifting) timed out with residual force 0.217346 eV/A.

**Caveats:** Not an optimized minimum; other more converged extraction states should be preferred.

### X06

**Location:** `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_6p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 6.0 Å above the median Pb(111) surface plane.

**Assessment:** Initial PbH2 extraction endpoint search, initially displaced by 6p0 A, with target mu=-0.11930 Ha. Final reported fmax 0.0236 eV/A after 33 FIRE steps; scheduler: COMPLETED. Produced a geometry/energy endpoint for first-stage extraction comparisons. Initial detachment difference relative to the same-mu precursor M2H07 is +1.208 eV; continued longer-distance endpoint X16 was also tested.

**Caveats:** Early continuum-only detachment benchmark, not a hydrated standard-state solution free energy; check product separation/charge.

### X07

**Location:** `surfaces/Pb111/fixed_mu/H_subsurface/deep/m0p1193`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Test whether the deep subsurface-H / Pb-lifted structure remains a local minimum at target-mu = -0.1193 Ha.

**Assessment:** Candidate subsurface-hydrogen / Pb-lifted configuration, initial designation continued deep-H structure. target mu=-0.11930 Ha. Final reported fmax 0.0358 eV/A after 3 FIRE steps; scheduler: COMPLETED. Used to test whether hydrogen incorporation beneath the first Pb layer is competitive with surface adsorption.

**Caveats:** Verify whether H remains subsurface versus emerging to the surface; compare with matched one-H same-mu endpoints, not neutral values across ensembles.

### X08

**Location:** `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p11195`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor.

**Assessment:** Early continuum-only potential-sweep endpoint for strongly lifted surface Pb(H)2 precursor at target mu=-0.11195 Ha. G=-2140.429250313 Ha; Final reported fmax 0.0394 eV/A after 46 FIRE steps; scheduler: COMPLETED. Matched early-model detached-minus-precursor difference is +16.886 eV (X12 paired); this is only a numerical contrast, not a validated dissolution free energy. The multi-eV difference is inconsistent with the later hydrated terrace series and flags a likely model/electronic-state artifact.

**Caveats:** Early continuum-only model: do not combine with explicit-water endpoint thermodynamics or treat extreme energy separations as physical before charge/cavity audit.

### X09

**Location:** `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor.

**Assessment:** Early continuum-only potential-sweep endpoint for strongly lifted surface Pb(H)2 precursor at target mu=-0.10460 Ha. G=-2144.144582290 Ha; Final reported fmax 0.0325 eV/A after 57 FIRE steps; scheduler: COMPLETED. Matched early-model detached-minus-precursor difference is +16.299 eV (X13 paired); this is only a numerical contrast, not a validated dissolution free energy. The multi-eV difference is inconsistent with the later hydrated terrace series and flags a likely model/electronic-state artifact.

**Caveats:** Early continuum-only model: do not combine with explicit-water endpoint thermodynamics or treat extreme energy separations as physical before charge/cavity audit.

### X10

**Location:** `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p09725`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor.

**Assessment:** Early continuum-only potential-sweep endpoint for strongly lifted surface Pb(H)2 precursor at target mu=-0.09725 Ha. G=-2147.864593644 Ha; Final reported fmax 0.0317 eV/A after 46 FIRE steps; scheduler: COMPLETED. Matched early-model detached-minus-precursor difference is +15.706 eV (X14 paired); this is only a numerical contrast, not a validated dissolution free energy. The multi-eV difference is inconsistent with the later hydrated terrace series and flags a likely model/electronic-state artifact.

**Caveats:** Early continuum-only model: do not combine with explicit-water endpoint thermodynamics or treat extreme energy separations as physical before charge/cavity audit.

### X11

**Location:** `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor.

**Assessment:** Early continuum-only potential-sweep endpoint for strongly lifted surface Pb(H)2 precursor at target mu=-0.08990 Ha. G=-2151.595225460 Ha; Final reported fmax 0.0316 eV/A after 56 FIRE steps; scheduler: COMPLETED. Matched early-model detached-minus-precursor difference is +2.424 eV (X15 paired); this is only a numerical contrast, not a validated dissolution free energy.

**Caveats:** Early continuum-only model: do not combine with explicit-water endpoint thermodynamics or treat extreme energy separations as physical before charge/cavity audit.

### X12

**Location:** `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p11195`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy.

**Assessment:** Early continuum-only potential-sweep endpoint for separated PbH2 plus vacancy at target mu=-0.11195 Ha. G=-2139.808717277 Ha; Final reported fmax 0.0388 eV/A after 5 FIRE steps; scheduler: COMPLETED. Matched early-model detached-minus-precursor difference is +16.886 eV (X08 paired); this is only a numerical contrast, not a validated dissolution free energy. The multi-eV difference is inconsistent with the later hydrated terrace series and flags a likely model/electronic-state artifact.

**Caveats:** Early continuum-only model: do not combine with explicit-water endpoint thermodynamics or treat extreme energy separations as physical before charge/cavity audit.

### X13

**Location:** `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy.

**Assessment:** Early continuum-only potential-sweep endpoint for separated PbH2 plus vacancy at target mu=-0.10460 Ha. G=-2143.545592742 Ha; Final reported fmax 0.0290 eV/A after 10 FIRE steps; scheduler: COMPLETED. Matched early-model detached-minus-precursor difference is +16.299 eV (X09 paired); this is only a numerical contrast, not a validated dissolution free energy. The multi-eV difference is inconsistent with the later hydrated terrace series and flags a likely model/electronic-state artifact.

**Caveats:** Early continuum-only model: do not combine with explicit-water endpoint thermodynamics or treat extreme energy separations as physical before charge/cavity audit.

### X14

**Location:** `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p09725`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy.

**Assessment:** Early continuum-only potential-sweep endpoint for separated PbH2 plus vacancy at target mu=-0.09725 Ha. G=-2147.287402467 Ha; Final reported fmax 0.0395 eV/A after 10 FIRE steps; scheduler: COMPLETED. Matched early-model detached-minus-precursor difference is +15.706 eV (X10 paired); this is only a numerical contrast, not a validated dissolution free energy. The multi-eV difference is inconsistent with the later hydrated terrace series and flags a likely model/electronic-state artifact.

**Caveats:** Early continuum-only model: do not combine with explicit-water endpoint thermodynamics or treat extreme energy separations as physical before charge/cavity audit.

### X15

**Location:** `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p0899`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy.

**Assessment:** Early continuum-only potential-sweep endpoint for separated PbH2 plus vacancy at target mu=-0.08990 Ha. G=-2151.506137430 Ha; Final reported fmax 0.0390 eV/A after 45 FIRE steps; scheduler: COMPLETED. Matched early-model detached-minus-precursor difference is +2.424 eV (X11 paired); this is only a numerical contrast, not a validated dissolution free energy.

**Caveats:** Early continuum-only model: do not combine with explicit-water endpoint thermodynamics or treat extreme energy separations as physical before charge/cavity audit.

### X16

**Location:** `surfaces/Pb111/PbH2_extraction/separation/fixed_mu/m0p1193/plus_1p5`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Separation-convergence check for detached PbH2 at target-mu = -0.1193 Ha; the intact PbH2 unit from X06 is translated 1.5 Å farther from the Pb(111) surface.

**Assessment:** Early continuum-only potential-sweep endpoint for separated PbH2 plus vacancy at target mu=-0.11930 Ha. G=-2136.077008548 Ha; Final reported fmax 0.0375 eV/A after 0 FIRE steps; scheduler: COMPLETED. This farther-separated product tests separation dependence at fixed mu; compared with X06 the difference is -0.001 eV.

**Caveats:** Early continuum-only model: do not combine with explicit-water endpoint thermodynamics or treat extreme energy separations as physical before charge/cavity audit.

### X17

**Location:** `surfaces/Pb111/fixed_mu/H2_reference/separated/m0p11195`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Test whether the separated two-H surface basin remains a physical local minimum at target-mu = -0.11195 Ha.

**Assessment:** Dry/fixed-potential separated two-H reference at -1.2 V RHE timed out with maximum force 0.079483 eV/A.

**Caveats:** Not converged to 0.04 eV/A and should not be treated as an optimized endpoint.

### X18

**Location:** `surfaces/Pb111/fixed_mu/H2_reference/same_Pb/m0p11195`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Test whether the same-Pb two-H surface basin remains a physical local minimum at target-mu = -0.11195 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as surfaces, at target mu=-0.11195 Ha. G=-2139.850011224 Ha, +7.713 eV relative to lowest two-H numerical value for this mu (X17); Final reported fmax 0.0345 eV/A after 7 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units. Multi-eV separation among nominally comparable two-H surfaces is suspicious; do not interpret it as a normal adsorption-site preference.

**Caveats:** CRITICAL: cross-check electronic population, cavity construction, and final state before including this G difference in a thermodynamic comparison.

### X19

**Location:** `surfaces/Pb111/fixed_mu/H2_reference/separated/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Continue a chemically valid separated two-H surface state to target-mu = -0.09725 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as surfaces, at target mu=-0.09725 Ha. G=-2147.324723868 Ha, +0.000 eV relative to lowest two-H numerical value for this mu (X19); Final reported fmax 0.0358 eV/A after 8 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units.

**Caveats:** Same-mu energy comparison is preliminary; the starting site name may not identify the relaxed minimum and dry-model results do not substitute for hydrated calculations.

### X20

**Location:** `surfaces/Pb111/fixed_mu/H2_reference/same_Pb/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether the same-Pb two-H surface basin survives at target-mu = -0.09725 Ha.

**Assessment:** Two-H grand-canonical adsorption precursor initialized as surfaces, at target mu=-0.09725 Ha. G=-2147.324693638 Ha, +0.001 eV relative to lowest two-H numerical value for this mu (X19); Final reported fmax 0.0344 eV/A after 22 FIRE steps; scheduler: COMPLETED. The geometry is relevant to H migration, Tafel recombination, and formation of same-Pb Pb(H)2 units.

**Caveats:** Same-mu energy comparison is preliminary; the starting site name may not identify the relaxed minimum and dry-model results do not substitute for hydrated calculations.

### X21

**Location:** `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p1193`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Test whether two explicit first-shell water molecules prevent the CANDLE proton-well artifact for strongly lifted surface Pb(H)2 at fixed electron chemical potential.

**Assessment:** Hydrated hydride-oriented terrace precursor at -1.0 V RHE. Converged fmax 0.030990 eV/A; matched to detached product X28 for +1.309621 eV detachment grand-potential difference.

**Caveats:** Retain matched stoichiometry/electron chemical potential; precursor structure and explicit water integrity should be checked again in complete publication audit.

### X22

**Location:** `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether two explicit first-shell water molecules prevent the CANDLE proton-well artifact for strongly lifted surface Pb(H)2 at fixed electron chemical potential.

**Assessment:** Hydrated hydride-oriented terrace precursor at -1.6 V RHE; matched to detached X29, endpoint detachment grand potential +1.432054 eV.

**Caveats:** Matched endpoint thermodynamics, not a kinetic activation barrier.

### X23

**Location:** `surfaces/Pb111/proton_well_rescue/proton_oriented/m0p1193`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Test whether two explicit first-shell water molecules prevent the CANDLE proton-well artifact for strongly lifted surface Pb(H)2 at fixed electron chemical potential.

**Assessment:** Proton-oriented explicit-water terrace trial at -1.0 V RHE timed out, with final reported optimizer force 0.208222 eV/A.

**Caveats:** Not converged; do not extract thermodynamics from this output without additional numerical/structural review.

### X24

**Location:** `surfaces/Pb111/proton_well_rescue/proton_oriented/m0p09725`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Test whether two explicit first-shell water molecules prevent the CANDLE proton-well artifact for strongly lifted surface Pb(H)2 at fixed electron chemical potential.

**Assessment:** Proton-oriented explicit-water terrace trial at -1.6 V RHE timed out with extreme residual force 13.416493 eV/A.

**Caveats:** Numerically unreliable; do not interpret this unconverged geometry or energy as a physical minimum.

### X25

**Location:** `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p11195`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Continue the successful hydride-oriented explicit-water Pb(H)2 branch across fixed electron chemical potential to test whether first-shell water suppresses the CANDLE proton-well artifact.

**Assessment:** Hydrated hydride-oriented terrace precursor at -1.2 V RHE; matched to detached X30, endpoint detachment grand potential +1.318411 eV.

**Caveats:** Matched endpoint thermodynamics, not a kinetic activation barrier.

### X26

**Location:** `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p1046`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Continue the successful hydride-oriented explicit-water Pb(H)2 branch across fixed electron chemical potential to test whether first-shell water suppresses the CANDLE proton-well artifact.

**Assessment:** Hydrated hydride-oriented terrace precursor at -1.4 V RHE; matched to detached X31, endpoint detachment grand potential +1.356592 eV.

**Caveats:** Matched endpoint thermodynamics, not a kinetic activation barrier.

### X27

**Location:** `surfaces/Pb111/proton_well_rescue/hydride_oriented/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Continue the successful hydride-oriented explicit-water Pb(H)2 branch across fixed electron chemical potential to test whether first-shell water suppresses the CANDLE proton-well artifact.

**Assessment:** Hydrated hydride-oriented terrace precursor at -1.8 V RHE; matched to detached X32, endpoint detachment grand potential +1.554947 eV.

**Caveats:** Matched endpoint thermodynamics remain useful even though hydrated terrace extraction NEB at this potential was invalid.

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

### X33

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p1193`. **Priority:** diagnostic. **Review state:** superseded.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** Hydrated FCC-adatom PbH2 precursor at target mu=-0.11930 Ha, with two explicit waters. G=-2228.097714557 Ha; Final reported fmax 0.0903 eV/A after 87 FIRE steps; scheduler: TIMEOUT. This is the initial precursor optimization, subsequently continued because the original run timed out.

**Caveats:** Not converged to nominal 0.04 eV/A. Use the later continuation rather than this original endpoint for thermodynamics; final structural identity still needs inspection.

### X34

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p1193`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** Hydrated FCC-adatom PbH2 detached product at target mu=-0.11930 Ha, with two explicit waters. G=-2228.065227538 Ha; Final reported fmax 0.0333 eV/A after 42 FIRE steps; scheduler: COMPLETED. The extracted local detachment G difference relative to X78 is +0.965 eV.

**Caveats:** Final detached PbH2 geometry and electronic/solvation branch must be audited; local adatom extraction omits cost of producing the adatom and bulk-solution standard-state terms.

### X35

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p11195`. **Priority:** diagnostic. **Review state:** superseded.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** Hydrated FCC-adatom PbH2 precursor at target mu=-0.11195 Ha, with two explicit waters. G=-2232.051515882 Ha; Final reported fmax 0.0513 eV/A after 103 FIRE steps; scheduler: TIMEOUT. This is the initial precursor optimization, subsequently continued because the original run timed out.

**Caveats:** Not converged to nominal 0.04 eV/A. Use the later continuation rather than this original endpoint for thermodynamics; final structural identity still needs inspection.

### X36

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p11195`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** Hydrated FCC-adatom PbH2 detached product at target mu=-0.11195 Ha, with two explicit waters. G=-2232.018990644 Ha; Final reported fmax 0.0367 eV/A after 37 FIRE steps; scheduler: COMPLETED. The extracted local detachment G difference relative to X79 is +0.919 eV.

**Caveats:** Final detached PbH2 geometry and electronic/solvation branch must be audited; local adatom extraction omits cost of producing the adatom and bulk-solution standard-state terms.

### X37

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p1046`. **Priority:** diagnostic. **Review state:** superseded.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** Hydrated FCC-adatom PbH2 precursor at target mu=-0.10460 Ha, with two explicit waters. G=-2236.008382470 Ha; Final reported fmax 0.0557 eV/A after 104 FIRE steps; scheduler: TIMEOUT. This is the initial precursor optimization, subsequently continued because the original run timed out.

**Caveats:** Not converged to nominal 0.04 eV/A. Use the later continuation rather than this original endpoint for thermodynamics; final structural identity still needs inspection.

### X38

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p1046`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** Hydrated FCC-adatom PbH2 detached product at target mu=-0.10460 Ha, with two explicit waters. G=-2235.976819557 Ha; Final reported fmax 0.0345 eV/A after 31 FIRE steps; scheduler: COMPLETED. The extracted local detachment G difference relative to X80 is +0.908 eV.

**Caveats:** Final detached PbH2 geometry and electronic/solvation branch must be audited; local adatom extraction omits cost of producing the adatom and bulk-solution standard-state terms.

### X39

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p09725`. **Priority:** diagnostic. **Review state:** superseded.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** Hydrated FCC-adatom PbH2 precursor at target mu=-0.09725 Ha, with two explicit waters. G=-2239.971557482 Ha; Final reported fmax 0.0551 eV/A after 101 FIRE steps; scheduler: TIMEOUT. This is the initial precursor optimization, subsequently continued because the original run timed out.

**Caveats:** Not converged to nominal 0.04 eV/A. Use the later continuation rather than this original endpoint for thermodynamics; final structural identity still needs inspection.

### X40

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** Hydrated FCC-adatom PbH2 detached product at target mu=-0.09725 Ha, with two explicit waters. G=-2239.938424700 Ha; Final reported fmax 0.0215 eV/A after 33 FIRE steps; scheduler: COMPLETED. The extracted local detachment G difference relative to X81 is +0.921 eV.

**Caveats:** Final detached PbH2 geometry and electronic/solvation branch must be audited; local adatom extraction omits cost of producing the adatom and bulk-solution standard-state terms.

### X41

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** FCC-adatom hydrated Pb(H)2 precursor at -1.8 V RHE; matched detached structure X42 gives +0.946463 eV local detachment grand potential.

**Caveats:** NEB connecting X41 to X42 exhibited an abrupt dielectric/charge change. Check the precursor geometry and defect thermodynamic cycle.

### X42

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** FCC-adatom hydrated detached PbH2 endpoint at -1.8 V RHE; energy pairing with X41 gives +0.946463 eV local extraction cost.

**Caveats:** Endpoint thermodynamics do not establish an adatom creation or dissolution rate.

### X43

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p1193`. **Priority:** supporting. **Review state:** superseded.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** Original hydrated HCP-adatom PbH2 precursor at -1.0 V RHE; its paired X44 detachment cost is +0.552896 eV, but a later independent relaxation from the NEB found lower-energy precursor X86.

**Caveats:** Use X86 rather than X43 for the revised HCP-adatom detachment reaction; X43 remains a distinct local structure.

### X44

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p1193`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** Hydrated HCP-adatom detached PbH2 endpoint at -1.0 V RHE, paired with optimized precursor X86; local detachment grand potential +0.880822 eV.

**Caveats:** Pre-existing adatom. Does not include the energy of creating an adatom/vacancy defect.

### X45

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p11195`. **Priority:** diagnostic. **Review state:** superseded.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** Hydrated HCP-adatom PbH2 precursor at target mu=-0.11195 Ha, with two explicit waters. G=-2232.047703545 Ha; Final reported fmax 0.0710 eV/A after 92 FIRE steps; scheduler: TIMEOUT. This is the initial precursor optimization, subsequently continued because the original run timed out.

**Caveats:** Not converged to nominal 0.04 eV/A. Use the later continuation rather than this original endpoint for thermodynamics; final structural identity still needs inspection.

### X46

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p11195`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** Hydrated HCP-adatom PbH2 detached product at target mu=-0.11195 Ha, with two explicit waters. G=-2232.019030026 Ha; Final reported fmax 0.0383 eV/A after 36 FIRE steps; scheduler: COMPLETED. The extracted local detachment G difference relative to X82 is +0.902 eV.

**Caveats:** Final detached PbH2 geometry and electronic/solvation branch must be audited; local adatom extraction omits cost of producing the adatom and bulk-solution standard-state terms.

### X47

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p1046`. **Priority:** diagnostic. **Review state:** superseded.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** Hydrated HCP-adatom PbH2 precursor at target mu=-0.10460 Ha, with two explicit waters. G=-2236.006713121 Ha; Final reported fmax 0.0693 eV/A after 92 FIRE steps; scheduler: TIMEOUT. This is the initial precursor optimization, subsequently continued because the original run timed out.

**Caveats:** Not converged to nominal 0.04 eV/A. Use the later continuation rather than this original endpoint for thermodynamics; final structural identity still needs inspection.

### X48

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p1046`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** Hydrated HCP-adatom PbH2 detached product at target mu=-0.10460 Ha, with two explicit waters. G=-2235.976837749 Ha; Final reported fmax 0.0303 eV/A after 26 FIRE steps; scheduler: COMPLETED. The extracted local detachment G difference relative to X83 is +0.881 eV.

**Caveats:** Final detached PbH2 geometry and electronic/solvation branch must be audited; local adatom extraction omits cost of producing the adatom and bulk-solution standard-state terms.

### X49

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p09725`. **Priority:** diagnostic. **Review state:** superseded.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** Hydrated HCP-adatom PbH2 precursor at target mu=-0.09725 Ha, with two explicit waters. G=-2239.971580336 Ha; Final reported fmax 0.0795 eV/A after 93 FIRE steps; scheduler: TIMEOUT. This is the initial precursor optimization, subsequently continued because the original run timed out.

**Caveats:** Not converged to nominal 0.04 eV/A. Use the later continuation rather than this original endpoint for thermodynamics; final structural identity still needs inspection.

### X50

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** Hydrated HCP-adatom PbH2 detached product at target mu=-0.09725 Ha, with two explicit waters. G=-2239.938312278 Ha; Final reported fmax 0.0332 eV/A after 24 FIRE steps; scheduler: COMPLETED. The extracted local detachment G difference relative to X84 is +0.931 eV.

**Caveats:** Final detached PbH2 geometry and electronic/solvation branch must be audited; local adatom extraction omits cost of producing the adatom and bulk-solution standard-state terms.

### X51

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p0899`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** HCP-adatom PbH2 precursor trial at -1.8 V RHE timed out with residual force 0.724719 eV/A.

**Caveats:** Not converged; chemical validity unverified. Do not use for thermodynamic pair calculations.

### X52

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom.

**Assessment:** Hydrated HCP-adatom PbH2 detached product at target mu=-0.08990 Ha, with two explicit waters. G=-2243.903504818 Ha; Final reported fmax 0.0316 eV/A after 23 FIRE steps; scheduler: COMPLETED. The extracted local detachment G difference relative to X51 is +1.384 eV.

**Caveats:** Final detached PbH2 geometry and electronic/solvation branch must be audited; local adatom extraction omits cost of producing the adatom and bulk-solution standard-state terms.

### X53

**Location:** `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1193/z4p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential.

**Assessment:** Continuum-only Tafel molecular-H2 endpoint initialized 4.0 A above Pb(111) at target mu=-0.11930 Ha. G=-2136.168357293 Ha; Final reported fmax 0.0398 eV/A after 25 FIRE steps; scheduler: COMPLETED. Alternative starting separation X54 differs by -0.021 eV in final G.

**Caveats:** A valid H2 product endpoint does not validate the corresponding dry NEB, whose intermediate proton-well structures were invalid; product height/orientation and charge must be examined.

### X54

**Location:** `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1193/z6p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential.

**Assessment:** Continuum-only Tafel molecular-H2 endpoint initialized 6.0 A above Pb(111) at target mu=-0.11930 Ha. G=-2136.167587531 Ha; Final reported fmax 0.0244 eV/A after 26 FIRE steps; scheduler: COMPLETED. Alternative starting separation X53 differs by +0.021 eV in final G.

**Caveats:** A valid H2 product endpoint does not validate the corresponding dry NEB, whose intermediate proton-well structures were invalid; product height/orientation and charge must be examined.

### X55

**Location:** `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p11195/z4p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential.

**Assessment:** Continuum-only Tafel molecular-H2 endpoint initialized 4.0 A above Pb(111) at target mu=-0.11195 Ha. G=-2139.898321554 Ha; Final reported fmax 0.0359 eV/A after 23 FIRE steps; scheduler: COMPLETED. Alternative starting separation X56 differs by +0.024 eV in final G.

**Caveats:** A valid H2 product endpoint does not validate the corresponding dry NEB, whose intermediate proton-well structures were invalid; product height/orientation and charge must be examined.

### X56

**Location:** `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p11195/z6p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential.

**Assessment:** Continuum-only Tafel molecular-H2 endpoint initialized 6.0 A above Pb(111) at target mu=-0.11195 Ha. G=-2139.899200649 Ha; Final reported fmax 0.0372 eV/A after 27 FIRE steps; scheduler: COMPLETED. Alternative starting separation X55 differs by -0.024 eV in final G.

**Caveats:** A valid H2 product endpoint does not validate the corresponding dry NEB, whose intermediate proton-well structures were invalid; product height/orientation and charge must be examined.

### X57

**Location:** `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1046/z4p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential.

**Assessment:** Continuum-only Tafel molecular-H2 endpoint initialized 4.0 A above Pb(111) at target mu=-0.10460 Ha. G=-2143.634584825 Ha; Final reported fmax 0.0391 eV/A after 27 FIRE steps; scheduler: COMPLETED. Alternative starting separation X58 differs by +0.028 eV in final G.

**Caveats:** A valid H2 product endpoint does not validate the corresponding dry NEB, whose intermediate proton-well structures were invalid; product height/orientation and charge must be examined.

### X58

**Location:** `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1046/z6p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential.

**Assessment:** Continuum-only Tafel molecular-H2 endpoint initialized 6.0 A above Pb(111) at target mu=-0.10460 Ha. G=-2143.635599653 Ha; Final reported fmax 0.0386 eV/A after 21 FIRE steps; scheduler: COMPLETED. Alternative starting separation X57 differs by -0.028 eV in final G.

**Caveats:** A valid H2 product endpoint does not validate the corresponding dry NEB, whose intermediate proton-well structures were invalid; product height/orientation and charge must be examined.

### X59

**Location:** `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p09725/z4p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential.

**Assessment:** Continuum-only Tafel molecular-H2 endpoint initialized 4.0 A above Pb(111) at target mu=-0.09725 Ha. G=-2147.375506383 Ha; Final reported fmax 0.0299 eV/A after 25 FIRE steps; scheduler: COMPLETED. Alternative starting separation X60 differs by +0.024 eV in final G.

**Caveats:** A valid H2 product endpoint does not validate the corresponding dry NEB, whose intermediate proton-well structures were invalid; product height/orientation and charge must be examined.

### X60

**Location:** `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p09725/z6p0`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential.

**Assessment:** Continuum-only Tafel molecular-H2 endpoint initialized 6.0 A above Pb(111) at target mu=-0.09725 Ha. G=-2147.376377596 Ha; Final reported fmax 0.0310 eV/A after 29 FIRE steps; scheduler: COMPLETED. Alternative starting separation X59 differs by -0.024 eV in final G.

**Caveats:** A valid H2 product endpoint does not validate the corresponding dry NEB, whose intermediate proton-well structures were invalid; product height/orientation and charge must be examined.

### X61

**Location:** `surfaces/Pb111/fixed_mu/clean/m0p11195`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Fixed-electron-chemical-potential clean Pb(111) slab reference at target mu=-0.11195 Ha; G=-2138.958056941 Ha. Final reported fmax 0.0369 eV/A after 5 FIRE steps; scheduler: COMPLETED. Provides clean-surface grand potential for matched adsorbate/defect cycles.

**Caveats:** Reference calculations have different equilibrium electron counts at different mu; G values at different potentials are not direct reaction energies.

### X62

**Location:** `surfaces/Pb111/fixed_mu/clean/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Fixed-electron-chemical-potential clean Pb(111) slab reference at target mu=-0.09725 Ha; G=-2146.403956875 Ha. Final reported fmax 0.0385 eV/A after 1 FIRE steps; scheduler: COMPLETED. Provides clean-surface grand potential for matched adsorbate/defect cycles.

**Caveats:** Reference calculations have different equilibrium electron counts at different mu; G values at different potentials are not direct reaction energies.

### X63

**Location:** `surfaces/Pb111/fixed_mu/defects/vacancy/m0p1193`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface vacancy reference at target mu=-0.11930 Ha. G=-2075.911585965 Ha; Final reported fmax 0.0368 eV/A after 0 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X64

**Location:** `surfaces/Pb111/fixed_mu/defects/vacancy/m0p11195`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface vacancy reference at target mu=-0.11195 Ha. G=-2079.523757426 Ha; Final reported fmax 0.0357 eV/A after 6 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X65

**Location:** `surfaces/Pb111/fixed_mu/defects/vacancy/m0p1046`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface vacancy reference at target mu=-0.10460 Ha. G=-2083.141371824 Ha; Final reported fmax 0.0293 eV/A after 10 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X66

**Location:** `surfaces/Pb111/fixed_mu/defects/vacancy/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface vacancy reference at target mu=-0.09725 Ha. G=-2086.763227176 Ha; Final reported fmax 0.0372 eV/A after 8 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X67

**Location:** `surfaces/Pb111/fixed_mu/defects/vacancy/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface vacancy reference at target mu=-0.08990 Ha. G=-2090.389758075 Ha; Final reported fmax 0.0370 eV/A after 9 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X68

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p1193`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface FCC adatom reference at target mu=-0.11930 Ha. G=-2194.535290706 Ha; Final reported fmax 0.0346 eV/A after 4 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X69

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p11195`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface FCC adatom reference at target mu=-0.11195 Ha. G=-2198.355268456 Ha; Final reported fmax 0.0394 eV/A after 5 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X70

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p1046`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface FCC adatom reference at target mu=-0.10460 Ha. G=-2202.180457515 Ha; Final reported fmax 0.0337 eV/A after 5 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X71

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface FCC adatom reference at target mu=-0.09725 Ha. G=-2206.010257981 Ha; Final reported fmax 0.0377 eV/A after 16 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X72

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface FCC adatom reference at target mu=-0.08990 Ha. G=-2209.844160134 Ha; Final reported fmax 0.0282 eV/A after 21 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X73

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p1193`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface HCP adatom reference at target mu=-0.11930 Ha. G=-2194.535169654 Ha; Final reported fmax 0.0364 eV/A after 11 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X74

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p11195`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface HCP adatom reference at target mu=-0.11195 Ha. G=-2198.353814313 Ha; Final reported fmax 0.0399 eV/A after 21 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X75

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p1046`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface HCP adatom reference at target mu=-0.10460 Ha. G=-2202.178212325 Ha; Final reported fmax 0.0357 eV/A after 18 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X76

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface HCP adatom reference at target mu=-0.09725 Ha. G=-2206.007050204 Ha; Final reported fmax 0.0284 eV/A after 19 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X77

**Location:** `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p0899`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation.

**Assessment:** Grand-canonical, fixed-potential clean-surface HCP adatom reference at target mu=-0.08990 Ha. G=-2209.840782356 Ha; Final reported fmax 0.0271 eV/A after 20 FIRE steps; scheduler: COMPLETED. Used with matched clean surface and other defect states in the balanced surface-vacancy/adatom formation cycle.

**Caveats:** Single defect G values cannot be interpreted as isolated vacancy or adatom formation energies because Pb stoichiometry differs; use an explicitly balanced same-mu cycle.

### X78

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p1193`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings.

**Assessment:** Hydrated FCC-adatom PbH2 continued optimization of a prior timed-out precursor at target mu=-0.11930 Ha, with two explicit waters. G=-2228.100701189 Ha; Final reported fmax 0.0376 eV/A after 41 FIRE steps; scheduler: COMPLETED. Continued the earlier precursor trial X33; final G changed by -0.081 eV.

**Caveats:** Numerical convergence of the continuation is observed; check final Pb-H connectivity, water integrity, charge state, and competing precursor minima before using it in a kinetic cycle.

### X79

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p11195`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings.

**Assessment:** Hydrated FCC-adatom PbH2 continued optimization of a prior timed-out precursor at target mu=-0.11195 Ha, with two explicit waters. G=-2232.052776423 Ha; Final reported fmax 0.0356 eV/A after 33 FIRE steps; scheduler: COMPLETED. Continued the earlier precursor trial X35; final G changed by -0.034 eV.

**Caveats:** Numerical convergence of the continuation is observed; check final Pb-H connectivity, water integrity, charge state, and competing precursor minima before using it in a kinetic cycle.

### X80

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p1046`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings.

**Assessment:** Hydrated FCC-adatom PbH2 continued optimization of a prior timed-out precursor at target mu=-0.10460 Ha, with two explicit waters. G=-2236.010177321 Ha; Final reported fmax 0.0380 eV/A after 40 FIRE steps; scheduler: COMPLETED. Continued the earlier precursor trial X37; final G changed by -0.049 eV.

**Caveats:** Numerical convergence of the continuation is observed; check final Pb-H connectivity, water integrity, charge state, and competing precursor minima before using it in a kinetic cycle.

### X81

**Location:** `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings.

**Assessment:** Hydrated FCC-adatom PbH2 continued optimization of a prior timed-out precursor at target mu=-0.09725 Ha, with two explicit waters. G=-2239.972269498 Ha; Final reported fmax 0.0399 eV/A after 33 FIRE steps; scheduler: COMPLETED. Continued the earlier precursor trial X39; final G changed by -0.019 eV.

**Caveats:** Numerical convergence of the continuation is observed; check final Pb-H connectivity, water integrity, charge state, and competing precursor minima before using it in a kinetic cycle.

### X82

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p11195`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings.

**Assessment:** Hydrated HCP-adatom PbH2 continued optimization of a prior timed-out precursor at target mu=-0.11195 Ha, with two explicit waters. G=-2232.052176819 Ha; Final reported fmax 0.0386 eV/A after 55 FIRE steps; scheduler: COMPLETED. Continued the earlier precursor trial X45; final G changed by -0.122 eV.

**Caveats:** Numerical convergence of the continuation is observed; check final Pb-H connectivity, water integrity, charge state, and competing precursor minima before using it in a kinetic cycle.

### X83

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p1046`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings.

**Assessment:** Hydrated HCP-adatom PbH2 continued optimization of a prior timed-out precursor at target mu=-0.10460 Ha, with two explicit waters. G=-2236.009232056 Ha; Final reported fmax 0.0399 eV/A after 56 FIRE steps; scheduler: COMPLETED. Continued the earlier precursor trial X47; final G changed by -0.069 eV.

**Caveats:** Numerical convergence of the continuation is observed; check final Pb-H connectivity, water integrity, charge state, and competing precursor minima before using it in a kinetic cycle.

### X84

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p09725`. **Priority:** supporting. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings.

**Assessment:** Hydrated HCP-adatom PbH2 continued optimization of a prior timed-out precursor at target mu=-0.09725 Ha, with two explicit waters. G=-2239.972527021 Ha; Final reported fmax 0.0383 eV/A after 24 FIRE steps; scheduler: COMPLETED. Continued the earlier precursor trial X49; final G changed by -0.026 eV.

**Caveats:** Numerical convergence of the continuation is observed; check final Pb-H connectivity, water integrity, charge state, and competing precursor minima before using it in a kinetic cycle.

### X85

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p0899`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings.

**Assessment:** Follow-up HCP-adatom precursor relaxation at -1.8 V RHE timed out with residual force 2.896891 eV/A.

**Caveats:** Still unconverged; not a usable equilibrium precursor. Distinguish this from other successful precursor continuations.

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

### X92

**Location:** `surfaces/Pb111/PbH2_formation/explicit_water/m0p1193/relax_X21_hydride_with_X90_water`. **Priority:** core. **Review state:** provisional.

**Setup intent:** Test whether a terrace Pb(H)2-like precursor is a local minimum in the hydration environment of the independently optimized on-top two-H reactant X90.

**Assessment:** Converged hydrated Pb(H)2-like precursor at mu=-0.11930 Ha. Final fmax=0.036798 eV/A; Pb32-H38=1.987 A, Pb32-H39=2.046 A, H-H=2.642 A. G=-2168.788186367622 Ha. DeltaOmega vs X90=+0.139528 eV; 0.165826 eV below X21. Both waters intact; water oxygen displacements vs X90 are 0.342 and 0.315 A.

**Caveats:** Locally relaxed candidate minimum, not a vibrationally verified minimum. Formation barrier unknown. Solvation and electronic continuity along the reaction path remain to be checked.
