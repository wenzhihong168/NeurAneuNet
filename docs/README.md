# Documentation

Technical notes for the public NeurAneuNet research repository.

| Document | Purpose |
|:---|:---|
| [Data interface](DATA_INTERFACE.md) | Defines privacy-safe 3DRA, geometry, clinical, and PED planning inputs |
| [Experiment record](EXPERIMENT_RECORD.md) | Captures configurations, split hashes, checkpoints, and evaluation context |
| [Evaluation metrics](METRICS.md) | Separates segmentation, sizing, placement, and clinical-assistance outcomes |
| [Artifact manifest](ARTIFACT_MANIFEST.md) | Links cohorts, models, result tables, and figures |
| [Failure analysis](FAILURE_ANALYSIS.md) | Localizes errors across perception, geometry, planning, and interaction |
| [Reproducibility scope](REPRODUCIBILITY.md) | States deterministic controls and the public-release boundary |
| [Release checklist](RELEASE_CHECKLIST.md) | Verifies clinical safety, evidence lineage, and public artifacts |

## Recommended order

Define the data contract and patient split first, create an experiment record before training, evaluate each output with its designated metrics, then bind released results to immutable artifacts and review severe failures.
