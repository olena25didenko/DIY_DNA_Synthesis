# Data dictionary — reference_atlas.csv

One row per sequencing run. 7 metadata columns, then 16 features. Feature
definitions match `extract_features._batch_features` and
`synth_forensics.FEATURE_NAMES` exactly.

## Metadata

| Column | Type | Meaning |
|---|---|---|
| `batch_id` | str | Run accession (DRR/SRR/ERR). The grouping unit for leave-one-run-out. |
| `route_class` | str | Chemistry label: `column_phosphoramidite`, `photolithographic`, `array_electrochem`, `array_deposition`. |
| `study` | str | Source dataset: `masaki`, `filges`, `lietard`, `gimpel`. |
| `sublabel` | str | Finer label within a route (capping variant, vendor, or array condition). |
| `umi_clean` | bool | True if the run had UMI/duplex consensus. False = no UMI (class-level rates only). |
| `n_molecules` | int | Consensus molecules (UMI families) in the run. |
| `aligned_bases` | int | Total consensus bases aligned. The denominator for every per-base rate. |

## Features (16)

Group 1 — error-type spectrum

| Column | Definition |
|---|---|
| `del_frac` | Deletions as a fraction of all error events (del+ins+sub). |
| `ins_frac` | Insertions as a fraction of all error events. |
| `sub_frac` | Substitutions as a fraction of all error events. |
| `log_total_err` | log10 of total error rate = (del+ins+sub) / `aligned_bases`. |

Group 2 — substitution spectrum (fraction of substitution events per directed channel)

| Column | Definition |
|---|---|
| `sub_GtoA` | G→A substitutions / all substitutions. Capping-driven column marker. |
| `sub_GtoT` | G→T / all substitutions. Photolithographic (oxidative) marker. |
| `sub_CtoT` | C→T / all substitutions. |
| `sub_TtoC` | T→C / all substitutions. |
| `sub_AtoG` | A→G / all substitutions. |
| `sub_other` | All remaining substitution directions / all substitutions. |

Group 3 — positional gradient

| Column | Definition |
|---|---|
| `pos5p_slope` | Slope of deletion density vs normalised 5′→3′ position (10 bins). Positive = 5′-ward gradient (electrochemical signature). 0 if fewer than 20 deletions. |

Group 4 — truncation ladder

| Column | Definition |
|---|---|
| `trunc_n1_frac` | Molecules with exactly one deletion / molecules with any deletion (n−1 ladder). |
| `trunc_decay` | (molecules with 2 deletions) / (molecules with 1 deletion). Ladder decay. |

Group 5 — sequence-context conditioning

| Column | Definition |
|---|---|
| `homopolymer_enrich` | Homopolymer-context error enrichment: hp / (1−hp). Neutral 1.0 when no `ctx` column is available. |
| `gc_effect` | Fraction of errors in GC context. 0.0 when no `ctx` column is available. |

Group 6 — intra-molecule correlation

| Column | Definition |
|---|---|
| `intra_corr` | Dispersion of errors-per-molecule: (var − mean)/mean, clipped to [−1, 5]. >0 = clustered (over-dispersed). |

Note: `homopolymer_enrich`/`gc_effect` are neutral placeholders for runs whose
error tables lack a per-event `ctx` column; treat them as uninformative for those
runs rather than as measured zeros.
