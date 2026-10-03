# Experiment Record

Use one immutable record for every reported NeurAneuNet run.

## Identity

| Field | Value |
|:---|:---|
| Experiment ID |  |
| Git revision |  |
| Configuration hash |  |
| Data and annotation version |  |
| Patient-level split hash |  |
| Random seeds |  |
| Hardware and software environment |  |

## Pipeline configuration

- Preprocessing profile, voxel spacing, and orientation policy:
- Segmentation backbone and checkpoint selection rule:
- Centerline and morphometry configuration:
- Knowledge and device-prior version:
- Fusion and decision-head configuration:
- Missing-modality handling:

## Evaluation record

Report segmentation, PED classification, diameter, length, landing zones, and clinical assessment in separate blocks. For each block, record cohort, sample count, exclusions, metric implementation, confidence interval, and failure cases.

## Release gate

- [ ] Patient partitions are disjoint.
- [ ] Independent clinical cases were not used for model selection.
- [ ] Every table and figure maps to a saved evaluation artifact.
- [ ] Reported values are labeled published, reproduced, or newly estimated.
- [ ] No protected data or private path is present in exported artifacts.
