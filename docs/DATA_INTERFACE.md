# Data Interface

This specification defines the privacy-safe boundary between local neurovascular data and the future NeurAneuNet pipeline. No patient-level examples are distributed here.

## Sample record

| Field group | Required content |
|:---|:---|
| Identity | Non-identifying `case_id` unique within the study |
| Imaging | Preoperative 3DRA volume, voxel spacing, and orientation metadata |
| Anatomy | Aneurysm and parent-vessel masks or annotation references |
| Geometry | Centerline, neck, diameter, curvature, and landing-zone features |
| Clinical context | Publication-approved structured phenotype variables |
| Planning targets | PED class, diameter, length, and proximal/distal placement |
| Provenance | Acquisition site, preprocessing version, and annotation version |

## Split manifest

Each `case_id` belongs to exactly one of `train`, `validation`, `test`, or `independent_clinical`. Related scans and derived records must inherit the same assignment. The manifest is frozen before preprocessing statistics or model fitting are computed.

## Validation checks

- Image, mask, spacing, and orientation metadata are mutually consistent.
- Units are explicit for every geometric and device measurement.
- Missing clinical variables use a mask rather than an undocumented sentinel.
- Targets are unavailable to preprocessing and inference components.
- Identifiers, free text, acquisition headers, and private paths are removed before export.

## Public boundary

Only schemas, synthetic fixtures, and validation logic may enter the public repository. Clinical volumes, derived patient tables, split manifests, and checkpoints remain local unless separately approved.
