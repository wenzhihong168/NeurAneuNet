# Reproducibility scope

This repository currently exposes the published figures, citation metadata, and the intended package architecture. The model implementation and clinical data are not part of this release.

## Experimental units

- Split data at the patient level before preprocessing or augmentation.
- Keep the independent 21-case clinical cohort outside model development.
- Report segmentation, PED sizing, landing-zone, and clinician-assistance outcomes separately.

## Determinism controls

- Record random seeds, software versions, hardware, and preprocessing parameters.
- Freeze patient-level split manifests before training.
- Version model configuration, checkpoints, and evaluation outputs together.

## Data boundary

Clinical images, identifiers, derived patient-level tables, and trained checkpoints must remain outside the public repository unless a separate approved release is prepared.

## Intended release order

1. Configuration schemas and privacy-safe data interfaces
2. Evaluation metrics and tests
3. Inference pipeline
4. Training implementation and approved model weights
