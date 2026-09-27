# Contributing

Contributions should strengthen reproducibility without exposing clinical data or unpublished implementation details.

## Suitable contributions

- Documentation, configuration schemas, and privacy-safe data interfaces.
- Evaluation utilities for segmentation, device selection, morphometry, and landing-zone planning.
- Tests for geometry processing, metric computation, and deterministic experiment setup.
- Corrections that keep repository claims aligned with the published article.

## Research safeguards

- Do not commit patient images, identifiers, split manifests, checkpoints, or derived records.
- Keep train, validation, test, and independent clinical cohorts isolated at patient level.
- Report segmentation, device-planning, and clinical-assessment results separately.
- Label every value as published, reproduced, or newly estimated; include the protocol and uncertainty.

## Pull requests

Use a focused branch and describe the purpose, affected module, validation performed, and any change to reported results. Run formatting and tests when implementation files are available, and keep generated artifacts out of version control.
