# Failure Analysis

Aggregate performance is insufficient for a system that links segmentation to device planning. Failures should be localized to the earliest affected stage.

## Error taxonomy

| Stage | Failure examples | Minimum evidence |
|:---|:---|:---|
| Image preprocessing | Cropping, orientation, or intensity failure | Input overlay and preprocessing log |
| Segmentation | Missed aneurysm, vessel discontinuity, boundary leakage | Mask overlay, Dice, HD95 |
| Geometry | Broken centerline, unstable neck plane, biased diameter | 3D visualization and signed error |
| Device planning | Wrong class, diameter, length, or landing zone | Candidate ranking and target comparison |
| Clinical interaction | Low agreement, excess time, high workload | Case-level ratings without identifiers |

## Required stratification

Review performance by aneurysm size, location, morphology, parent-vessel complexity, image quality, and acquisition site when support permits. Small subgroups retain counts and uncertainty rather than a bare mean.

## Case review

For every severe miss, record the first failed stage, downstream effects, confidence, whether the case is out of distribution, and whether a clinician could detect the error before action. Do not expose clinical images without release approval.

## Corrective-action rule

A proposed correction must identify its target failure class and be evaluated on the frozen test and independent clinical cohorts. Do not remove difficult cases or tune clinical thresholds after review.
