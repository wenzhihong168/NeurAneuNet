# Evaluation Metrics

NeurAneuNet spans perception, geometric measurement, device selection, and clinical planning. Results should therefore be reported by output rather than collapsed into one score.

| Output | Primary metrics | Reporting unit |
|:---|:---|:---|
| Aneurysm and parent-vessel segmentation | Dice, sensitivity, specificity, HD95 | Patient and anatomical structure |
| PED type or size class | Accuracy, macro F1, confusion matrix | Patient |
| Device diameter and length | MAE, RMSE, signed error | Millimetres |
| Proximal and distal landing zones | Euclidean or centerline offset | Millimetres |
| Clinical recommendation | Agreement rate with confidence interval | Case and physician |
| Workflow impact | Planning time, NASA-TLX, paired difference | Case and physician |

## Reporting rules

1. Keep the **600-aneurysm development cohort**, **210 PED-treated cases**, and **21-case independent clinical cohort** distinct.
2. Compute confidence intervals at patient level; account for repeated physician ratings in clinical comparisons.
3. Report diameter and length separately, including signed error to reveal systematic over- or under-sizing.
4. Present segmentation failure cases alongside aggregate Dice and boundary metrics.
5. Label values as published, independently reproduced, or newly estimated.

## Minimum result record

Each result should identify the cohort, patient count, split definition, preprocessing version, checkpoint, metric implementation, uncertainty method, and inference configuration.
