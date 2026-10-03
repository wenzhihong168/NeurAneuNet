# Artifact Manifest

Every published NeurAneuNet result should resolve to an immutable chain from cohort definition to figure.

| Artifact | Visibility | Required identity |
|:---|:---:|:---|
| Cohort inventory | Private | Version, inclusion criteria, content hash |
| Patient split manifest | Private | Split hash and cohort counts |
| Preprocessing profile | Public-safe | Parameter set and software revision |
| Segmentation checkpoint | Controlled | Config, seed, split hash, weight hash |
| Geometry export | Private | Case key, algorithm version, unit schema |
| PED decision checkpoint | Controlled | Fusion config, target registry, weight hash |
| Evaluation table | Public-safe | Checkpoint hashes, cohort, metric version |
| Figure | Public | Source-table hash and rendering revision |

## Required metadata

Each record stores `artifact_id`, role, source artifact IDs, Git revision, configuration hash, content hash, creation time, responsible author, and access class. Hashes identify artifacts; filenames do not.

## Lineage rule

A clinical or performance claim is releasable only when its table can be reconstructed from a frozen cohort, split, preprocessing profile, and checkpoint. Derived geometry and physician-level assessments remain linked by non-identifying case keys.

## Integrity checks

- No artifact crosses an access boundary during export.
- Figure values match the referenced evaluation table.
- Checkpoint selection precedes independent clinical assessment.
- Replaced artifacts receive new IDs rather than overwriting prior records.
