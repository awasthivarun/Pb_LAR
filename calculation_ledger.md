# Pb_LAR calculation ledger

Generated from `calculation_ledger.json`. Edit reviews with `scripts/calculation_ledger.py review`.
Raw DFT data and original `metadata.json` files remain in the separate Pb_LAR calculation tree.
**A `COMPLETED` Slurm state is not equivalent to geometry/NEB convergence or scientific validation.**

Jobs indexed: **152**; job records awaiting scientific review: **106**.

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
| X01 | go | not_reviewed | unassigned | Neutral PbH2-extraction endpoint search with the Pb(H)2 moiety initially translated so its Pb atom is 2.5 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_2p5` |
| X02 | go | not_reviewed | unassigned | Neutral PbH2-extraction endpoint search with the Pb(H)2 moiety initially translated so its Pb atom is 4.0 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_4p0` |
| X03 | go | not_reviewed | unassigned | Neutral PbH2-extraction endpoint search with the Pb(H)2 moiety initially translated so its Pb atom is 6.0 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/neutral/Pb_lift_6p0` |
| X04 | go | not_reviewed | unassigned | Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 2.5 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_2p5` |
| X05 | go | provisional | diagnostic | Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 4.0 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_4p0` |
| X06 | go | not_reviewed | unassigned | Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 6.0 Å above the median Pb(111) surface plane. | `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_6p0` |

## PbH2_extraction_explicit_water

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X28 | go | validated | core | Construct a detached PbH2 + vacancy product with two hydride-oriented explicit first-shell water molecules so that PbH2 detachment can be compared against the hydrated surface Pb(H)2 precursor at identical stoichiometry and target-mu. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p1193` |
| X29 | go | validated | supporting | Construct a detached PbH2 + vacancy product with two hydride-oriented explicit first-shell water molecules so that PbH2 detachment can be compared against the hydrated surface Pb(H)2 precursor at identical stoichiometry and target-mu. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p09725` |
| X30 | go | validated | supporting | Continue the physical hydrated detached PbH2 branch to complete the fixed-mu detachment curve. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p11195` |
| X31 | go | validated | supporting | Continue the physical hydrated detached PbH2 branch to complete the fixed-mu detachment curve. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p1046` |
| X32 | go | validated | supporting | Continue the physical hydrated detached PbH2 branch to complete the fixed-mu detachment curve. | `surfaces/Pb111/PbH2_extraction/explicit_water/detached/m0p0899` |

## PbH2_potential_sweep

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X08 | go | not_reviewed | unassigned | Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor. | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p11195` |
| X09 | go | not_reviewed | unassigned | Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor. | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p1046` |
| X10 | go | not_reviewed | unassigned | Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor. | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p09725` |
| X11 | go | not_reviewed | unassigned | Potential-dependent relaxation of the strongly lifted surface Pb(H)2 precursor. | `surfaces/Pb111/PbH2_extraction/potential_sweep/precursor/m0p0899` |
| X12 | go | not_reviewed | unassigned | Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy. | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p11195` |
| X13 | go | not_reviewed | unassigned | Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy. | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p1046` |
| X14 | go | not_reviewed | unassigned | Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy. | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p09725` |
| X15 | go | not_reviewed | unassigned | Potential-dependent relaxation of detached PbH2 above a Pb(111) vacancy. | `surfaces/Pb111/PbH2_extraction/potential_sweep/detached/m0p0899` |
| X16 | go | not_reviewed | unassigned | Separation-convergence check for detached PbH2 at target-mu = -0.1193 Ha; the intact PbH2 unit from X06 is translated 1.5 Å farther from the Pb(111) surface. | `surfaces/Pb111/PbH2_extraction/separation/fixed_mu/m0p1193/plus_1p5` |

## adatom_PbH2_explicit_water

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X33 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p1193` |
| X34 | go | not_reviewed | unassigned | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p1193` |
| X35 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p11195` |
| X36 | go | not_reviewed | unassigned | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p11195` |
| X37 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p1046` |
| X38 | go | not_reviewed | unassigned | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p1046` |
| X39 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p09725` |
| X40 | go | not_reviewed | unassigned | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p09725` |
| X41 | go | provisional | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor/m0p0899` |
| X42 | go | provisional | supporting | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/detached/m0p0899` |
| X43 | go | superseded | supporting | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p1193` |
| X44 | go | provisional | core | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p1193` |
| X45 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p11195` |
| X46 | go | not_reviewed | unassigned | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p11195` |
| X47 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p1046` |
| X48 | go | not_reviewed | unassigned | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p1046` |
| X49 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p09725` |
| X50 | go | not_reviewed | unassigned | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p09725` |
| X51 | go | provisional | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p0899` |
| X52 | go | not_reviewed | unassigned | Test the thermodynamic cost of detaching hydrated PbH2 from a low-coordination Pb adatom. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/detached/m0p0899` |
| X78 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p1193` |
| X79 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p11195` |
| X80 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p1046` |
| X81 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/fcc/explicit_water/precursor_restart1/m0p09725` |
| X82 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p11195` |
| X83 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p1046` |
| X84 | go | not_reviewed | unassigned | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p09725` |
| X85 | go | provisional | diagnostic | Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential. Continued from the timed-out Wave-10 CONTCAR without changing the physical model or optimizer settings. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_restart1/m0p0899` |
| X86 | go | validated | supporting | Independently relax N12 NEB image 01 to determine whether its 0.157 eV stabilization represents a physical lower-energy precursor. | `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor_from_N12_image01/m0p1193` |

## bulk_reference

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| B01 | bulk_reference | not_reviewed | unassigned | Optimize the bulk FCC Pb lattice constant used to construct all Pb surface models. | `bulk/Pb_fcc` |

## clean

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| S01 | go | not_reviewed | unassigned | Primary clean Pb(111) parent: 4 layers, 4x4x1 k-point mesh. | `surfaces/Pb111/clean` |

## convergence

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| S02 | go | not_reviewed | unassigned | Clean Pb(111), 4 layers, denser 6x6x1 k-point sampling. | `surfaces/Pb111/convergence/4L_k6` |
| S03 | go | not_reviewed | unassigned | Clean Pb(111), 5 layers, slab-thickness comparison. | `surfaces/Pb111/convergence/5L_k4` |
| S04 | go | not_reviewed | unassigned | Clean Pb(111), 6 layers, slab-thickness comparison. | `surfaces/Pb111/convergence/6L_k4` |

## defect

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| D01 | go | not_reviewed | unassigned | Pb(111) with one top-layer Pb vacancy; corrosion/extraction endpoint reference. | `surfaces/Pb111/defects/vacancy` |
| D02 | go | not_reviewed | unassigned | Pb adatom initially placed at the Pb(111) fcc hollow. | `surfaces/Pb111/defects/adatom_fcc` |
| D03 | go | not_reviewed | unassigned | Pb adatom initially placed at the Pb(111) hcp hollow. | `surfaces/Pb111/defects/adatom_hcp` |

## fixed_mu_1H

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| MH01 | go | not_reviewed | unassigned | One-H Pb(111) ontop geometry relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p1193` |
| MH02 | go | not_reviewed | unassigned | One-H Pb(111) ontop geometry relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p1046` |
| MH03 | go | not_reviewed | unassigned | One-H Pb(111) ontop geometry relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/ontop/m0p0899` |
| MH04 | go | not_reviewed | unassigned | One-H Pb(111) bridge geometry relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p1193` |
| MH05 | go | not_reviewed | unassigned | One-H Pb(111) bridge geometry relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p1046` |
| MH06 | go | not_reviewed | unassigned | One-H Pb(111) bridge geometry relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/bridge/m0p0899` |
| MH07 | go | not_reviewed | unassigned | One-H Pb(111) fcc geometry relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p1193` |
| MH08 | go | not_reviewed | unassigned | One-H Pb(111) fcc geometry relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p1046` |
| MH09 | go | not_reviewed | unassigned | One-H Pb(111) fcc geometry relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/fcc/m0p0899` |
| MH10 | go | not_reviewed | unassigned | One-H Pb(111) hcp geometry relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p1193` |
| MH11 | go | not_reviewed | unassigned | One-H Pb(111) hcp geometry relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p1046` |
| MH12 | go | not_reviewed | unassigned | One-H Pb(111) hcp geometry relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H_adsorption/hcp/m0p0899` |

## fixed_mu_2H

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| M2H01 | go | not_reviewed | unassigned | Two-H candidate 'fcc_hcp' relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p1193` |
| M2H02 | go | not_reviewed | unassigned | Two-H candidate 'fcc_hcp' relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p1046` |
| M2H03 | go | not_reviewed | unassigned | Two-H candidate 'fcc_hcp' relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/fcc_hcp/m0p0899` |
| M2H04 | go | not_reviewed | unassigned | Two-H candidate 'shared_bridges' relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p1193` |
| M2H05 | go | not_reviewed | unassigned | Two-H candidate 'shared_bridges' relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p1046` |
| M2H06 | go | not_reviewed | unassigned | Two-H candidate 'shared_bridges' relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/shared_bridges/m0p0899` |
| M2H07 | go | not_reviewed | unassigned | Two-H candidate 'PbH2_like' relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p1193` |
| M2H08 | go | provisional | diagnostic | Two-H candidate 'PbH2_like' relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p1046` |
| M2H09 | go | not_reviewed | unassigned | Two-H candidate 'PbH2_like' relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p0899` |
| X17 | go | provisional | diagnostic | Test whether the separated two-H surface basin remains a physical local minimum at target-mu = -0.11195 Ha. | `surfaces/Pb111/fixed_mu/H2_reference/separated/m0p11195` |
| X18 | go | not_reviewed | unassigned | Test whether the same-Pb two-H surface basin remains a physical local minimum at target-mu = -0.11195 Ha. | `surfaces/Pb111/fixed_mu/H2_reference/same_Pb/m0p11195` |
| X19 | go | not_reviewed | unassigned | Continue a chemically valid separated two-H surface state to target-mu = -0.09725 Ha. | `surfaces/Pb111/fixed_mu/H2_reference/separated/m0p09725` |
| X20 | go | not_reviewed | unassigned | Test whether the same-Pb two-H surface basin survives at target-mu = -0.09725 Ha. | `surfaces/Pb111/fixed_mu/H2_reference/same_Pb/m0p09725` |

## fixed_mu_H2_endpoint

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X53 | go | not_reviewed | unassigned | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1193/z4p0` |
| X54 | go | not_reviewed | unassigned | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1193/z6p0` |
| X55 | go | not_reviewed | unassigned | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p11195/z4p0` |
| X56 | go | not_reviewed | unassigned | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p11195/z6p0` |
| X57 | go | not_reviewed | unassigned | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1046/z4p0` |
| X58 | go | not_reviewed | unassigned | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p1046/z6p0` |
| X59 | go | not_reviewed | unassigned | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p09725/z4p0` |
| X60 | go | not_reviewed | unassigned | Construct and relax a molecular-H2 product endpoint for the Tafel HER pathway at fixed electron chemical potential. | `surfaces/Pb111/HER/Tafel/H2_endpoint/m0p09725/z6p0` |

## fixed_mu_clean

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| G01 | go | not_reviewed | unassigned | Clean Pb(111) relaxed at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/clean/m0p1193` |
| G02 | go | not_reviewed | unassigned | Clean Pb(111) relaxed at target-mu = -0.1046 Ha. | `surfaces/Pb111/fixed_mu/clean/m0p1046` |
| G03 | go | not_reviewed | unassigned | Clean Pb(111) relaxed at target-mu = -0.0899 Ha. | `surfaces/Pb111/fixed_mu/clean/m0p0899` |
| X61 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/clean/m0p11195` |
| X62 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/clean/m0p09725` |

## fixed_mu_defect

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| X63 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p1193` |
| X64 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p11195` |
| X65 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p1046` |
| X66 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p09725` |
| X67 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/vacancy/m0p0899` |
| X68 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p1193` |
| X69 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p11195` |
| X70 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p1046` |
| X71 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p09725` |
| X72 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_fcc/m0p0899` |
| X73 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p1193` |
| X74 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p11195` |
| X75 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p1046` |
| X76 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p09725` |
| X77 | go | not_reviewed | unassigned | Determine fixed-electron-chemical-potential Pb(111) defect thermodynamics for balanced vacancy-adatom Frenkel-pair formation. | `surfaces/Pb111/fixed_mu/defects/adatom_hcp/m0p0899` |

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
| H01 | go | not_reviewed | unassigned | One H initially adsorbed at the Pb(111) ontop site. | `surfaces/Pb111/H_adsorption/ontop` |
| H02 | go | not_reviewed | unassigned | One H initially adsorbed at the Pb(111) bridge site. | `surfaces/Pb111/H_adsorption/bridge` |
| H03 | go | not_reviewed | unassigned | One H initially adsorbed at the Pb(111) fcc site. | `surfaces/Pb111/H_adsorption/fcc` |
| H04 | go | not_reviewed | unassigned | One H initially adsorbed at the Pb(111) hcp site. | `surfaces/Pb111/H_adsorption/hcp` |

## neutral_2H

| ID | Type | Scientific status | Priority | Setup purpose | Directory |
|---|---|---|---|---|---|
| HH01 | go | not_reviewed | unassigned | Two surface H atoms initially occupying neighboring FCC and HCP hollow environments. | `surfaces/Pb111/H2_candidates/fcc_hcp` |
| HH02 | go | not_reviewed | unassigned | Two H atoms initially placed at two bridge sites sharing the same top-layer Pb atom. | `surfaces/Pb111/H2_candidates/shared_bridges` |
| HH03 | go | not_reviewed | unassigned | Two H atoms initially arranged as a bent PbH2-like moiety on one top-layer Pb atom; Pb-H = 1.90 Å initial guess. | `surfaces/Pb111/H2_candidates/PbH2_like` |

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
| SH01 | go | not_reviewed | unassigned | One H initially placed halfway between the first and second Pb layers, laterally registered with the fcc surface site. | `surfaces/Pb111/H_subsurface/fcc` |
| SH02 | go | not_reviewed | unassigned | One H initially placed halfway between the first and second Pb layers, laterally registered with the hcp surface site. | `surfaces/Pb111/H_subsurface/hcp` |
| SH03 | go | not_reviewed | unassigned | One H initially placed halfway between the first and second Pb layers, laterally registered with the ontop surface site. | `surfaces/Pb111/H_subsurface/ontop` |
| X07 | go | not_reviewed | unassigned | Test whether the deep subsurface-H / Pb-lifted structure remains a local minimum at target-mu = -0.1193 Ha. | `surfaces/Pb111/fixed_mu/H_subsurface/deep/m0p1193` |

## Scientific notes

### M2H08

**Location:** `surfaces/Pb111/fixed_mu/H2_candidates/PbH2_like/m0p1046`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Two-H candidate 'PbH2_like' relaxed at target-mu = -0.1046 Ha.

**Assessment:** Earlier dry/fixed-potential PbH2-like surface GO at -1.4 V RHE timed out with maximum force 0.057769 eV/A.

**Caveats:** Not converged to the 0.04 eV/A GO criterion; not independently reviewed structurally.

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

### X05

**Location:** `surfaces/Pb111/PbH2_extraction/fixed_mu/m0p1193/Pb_lift_4p0`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Fixed-potential PbH2-extraction endpoint search at target-mu -0.1193 Ha with the Pb(H)2 moiety initially translated so its Pb atom is 4.0 Å above the median Pb(111) surface plane.

**Assessment:** Early fixed-potential PbH2 extraction endpoint trial (4.0 A lifting) timed out with residual force 0.217346 eV/A.

**Caveats:** Not an optimized minimum; other more converged extraction states should be preferred.

### X17

**Location:** `surfaces/Pb111/fixed_mu/H2_reference/separated/m0p11195`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Test whether the separated two-H surface basin remains a physical local minimum at target-mu = -0.11195 Ha.

**Assessment:** Dry/fixed-potential separated two-H reference at -1.2 V RHE timed out with maximum force 0.079483 eV/A.

**Caveats:** Not converged to 0.04 eV/A and should not be treated as an optimized endpoint.

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

### X51

**Location:** `surfaces/Pb111/adatom_PbH2/hcp/explicit_water/precursor/m0p0899`. **Priority:** diagnostic. **Review state:** provisional.

**Setup intent:** Test whether a low-coordination Pb adatom supports a hydrated PbH2-like precursor at fixed electron chemical potential.

**Assessment:** HCP-adatom PbH2 precursor trial at -1.8 V RHE timed out with residual force 0.724719 eV/A.

**Caveats:** Not converged; chemical validity unverified. Do not use for thermodynamic pair calculations.

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
