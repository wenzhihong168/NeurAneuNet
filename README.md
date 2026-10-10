<div align="center">

# NeurAneuNet

**Knowledge-enhanced multimodal planning for intracranial aneurysm intervention**

[![Paper](https://img.shields.io/badge/Paper-CNS_Neuroscience_&_Therapeutics-4C78A8?style=flat-square)](https://doi.org/10.1002/cns.71047)
[![Open Access](https://img.shields.io/badge/Open_Access-CC_BY_4.0-2A9D8F?style=flat-square)](https://doi.org/10.1002/cns.71047)
[![AneuFusion](https://img.shields.io/badge/Extension-AneuFusion-8B5CF6?style=flat-square)](#architecture--aneufusion)
[![Repository](https://img.shields.io/badge/Repository-public-2563EB?style=flat-square)](#codebase-blueprint)

<sub>3D-DSA · vascular geometry · clinical knowledge · PED planning</sub>

</div>

<p align="center">
  <img src="assets/graphical-abstract.png" alt="NeurAneuNet graphical abstract">
</p>

NeurAneuNet is an end-to-end decision-support framework that converts preoperative 3D rotational angiography into aneurysm segmentation, vascular measurements, PED sizing, and landing-zone recommendations.

The study addresses a practical gap between image analysis and procedural planning. Rather than stopping at lesion segmentation, the framework carries anatomical information forward into device selection and deployment guidance, allowing the complete planning chain to be evaluated against expert measurements, device choices, and physician workflow outcomes.

Developed in collaboration with **PLA General Hospital**, the project is organized around a clinically consequential question: how can a three-dimensional vascular image be transformed into a reproducible, inspectable, and physician-reviewable treatment plan? The answer requires more than a high Dice score. It requires consistent boundary reconstruction, physically meaningful centerlines and diameters, explicit device constraints, and a recommendation layer that remains sensitive to aneurysm morphology and parent-vessel geometry.

## Research overview

Pipeline embolization device planning is a coupled perception-and-decision problem. The selected device must cover the aneurysm neck, remain compatible with vessel diameter, accommodate local curvature, and provide proximal and distal landing zones that are technically plausible. Manual planning therefore combines image interpretation, geometric measurement, device knowledge, and operator experience. Small upstream errors can propagate: an uncertain aneurysm boundary changes neck localization; an unstable centerline alters diameter estimates; a biased diameter estimate can move the case across a device-size boundary.

NeurAneuNet models this dependency chain directly. The segmentation branch identifies the aneurysm and parent artery from 3DRA; the geometric branch converts the segmentation into quantitative vascular descriptors; the knowledge branch represents clinically relevant device and anatomy priors; and the multimodal decision network jointly predicts PED class, diameter, length, and landing positions. The framework is therefore evaluated at three connected levels: anatomical fidelity, device-planning accuracy, and physician-facing workflow performance.

The repository presents the work as an assistive planning system, not an autonomous procedural decision maker. The output is intended to structure and accelerate expert review. Difficult morphologies, weak boundaries, microaneurysms, lesions near bifurcations, and cases close to adjacent device thresholds remain situations in which the image, derived geometry, and alternative device candidates must be reviewed together.

## At a glance

<table align="center">
  <tr align="center">
    <th>Input</th><th>Core model</th><th>Outputs</th><th>Evaluation</th>
  </tr>
  <tr align="center">
    <td>3DRA, geometry,<br>clinical phenotype</td>
    <td>Dual-path U-Net++<br>tensor fusion · KAN</td>
    <td>Segmentation · PED size<br>diameter/length · landing zones</td>
    <td>Internal modeling<br>independent clinical assessment</td>
  </tr>
</table>

<table align="center">
  <tr align="center">
    <th>Development cohort</th><th>PED-treated subset</th><th>Model split</th><th>Independent clinical cohort</th>
  </tr>
  <tr align="center">
    <td><b>600 aneurysms</b></td><td><b>210 cases</b></td><td><b>147 / 21 / 42</b></td><td><b>21 cases · 6 physicians</b></td>
  </tr>
</table>

## Method

1. **Vascular perception** — adaptive preprocessing and dual-path attention U-Net++ segment aneurysms and parent vessels.
2. **Geometric reasoning** — centerlines, diameters, curvature, neck morphology, and candidate landing zones are derived from 3D anatomy.
3. **Knowledge enhancement** — structured vascular and device priors provide clinically meaningful constraints.
4. **Multimodal fusion** — image, geometric, temporal, clinical, and knowledge features interact through tensor decomposition.
5. **Treatment planning** — high-order KAN heads jointly predict PED type, diameter, length, and proximal/distal placement.

## Clinical problem formulation

### From 3DRA to an actionable vascular representation

The input is not treated as a generic volumetric classification sample. It is processed as a vascular scene in which the aneurysm sac, neck region, parent artery, local curvature, and candidate landing segments have distinct procedural meanings. The dual-path segmentation network is designed to preserve both global vessel continuity and fine aneurysm-boundary detail. Channel and spatial attention concentrate feature responses on foreground anatomy, while adversarial refinement encourages anatomically coherent masks in small or indistinct lesions.

The resulting mask is converted into a geometry-aware representation. Centerline extraction defines the longitudinal coordinate system of the parent vessel; cross-sectional measurements estimate local diameter; curvature and neck morphology describe the spatial difficulty of deployment; and proximal and distal candidate regions define where the device may be anchored. Keeping these quantities in physical units is important because clinically relevant errors occur at the millimeter scale and cannot be interpreted reliably from voxel overlap alone.

### Multimodal evidence and procedural knowledge

The planning stage combines five information streams: bottleneck image features, explicit vascular geometry, temporal or procedural descriptors, structured clinical variables, and device-related knowledge. These streams differ in dimension, scale, and semantics. A direct concatenation would allow high-dimensional image features to dominate the decision even when a low-dimensional geometric constraint is decisive. Tensor-decomposition fusion is therefore used to expose higher-order interactions while controlling the size of the joint representation.

This design is especially relevant for wide-neck, tortuous, or multi-lesion cases. In such settings, the correct device is not determined by a single measurement. Diameter, neck coverage, curvature, landing-zone length, and the available device catalogue interact. The fused representation provides the decision head with both anatomical evidence and structured constraints, allowing the recommendation to respond to the combination rather than treating every modality independently.

### Multi-output treatment planning

The decision network separates categorical and continuous outputs while training them as a connected task. Device model selection is optimized as a classification problem. Diameter and length are estimated through probabilistic regression, preserving uncertainty around continuous size predictions. Proximal and distal landing positions use geometry-aware objectives so that the final output remains tied to the reconstructed parent vessel.

The KAN-based head represents nonlinear, high-order relationships within the fused feature space. Sparse attention selects the interactions most relevant to a case, and task-specific branches map the shared representation to device identity, physical dimensions, and placement. Learnable loss weights balance the classification, regression, and positional objectives so that one numerically dominant task does not suppress the others.

## Architecture · AneuFusion

AneuFusion extends the shared neurovascular backbone with dual-pathway encoding, ML-KAN feature extraction, sparse attention, and tensor-decomposition fusion.

The architecture separates fine-grained vascular perception from higher-order clinical reasoning. Image features are integrated with geometric measurements, temporal descriptors, structured patient variables, and device knowledge before task-specific heads estimate PED type, diameter, length, and proximal/distal landing positions. This multimodal organization is intended to preserve anatomical detail while making the final recommendation responsive to procedural constraints.

<p align="center">
  <img src="assets/architecture.png" alt="AneuFusion multimodal architecture">
</p>

### Staged optimization strategy

The published training protocol decomposes optimization into five stages. Segmentation is first pretrained with complementary overlap, boundary, and structural-similarity objectives. An adversarial stage then refines the realism and continuity of predicted masks. Geometry extraction and knowledge enhancement are trained after a stable anatomical representation is available. Multimodal fusion and the KAN decision layer are optimized with the earlier modules temporarily fixed, followed by end-to-end fine-tuning of the complete system.

This schedule reflects the causal order of the workflow. The decision layer should not learn around a continually moving segmentation target, and geometric features should not be optimized before the underlying vascular surface is sufficiently stable. Final joint fine-tuning then allows downstream planning errors to adjust the upstream representation without discarding the anatomical priors established during pretraining.

### Output contract

For each case, the system produces an aneurysm and parent-vessel segmentation, derived morphometric measurements, a ranked device recommendation, diameter and length estimates, and proximal/distal landing positions. The primary quantitative evaluation uses the top-ranked recommendation. Alternative candidates and confidence values are intended to support review, not to retroactively increase reported accuracy.

## Published results

<table align="center">
  <tr align="center">
    <th>Segmentation Dice</th><th>PED classification</th><th>Diameter error</th><th>Primary recommendation</th>
  </tr>
  <tr align="center">
    <td><b>0.874 ± 0.03</b></td><td><b>91.8%</b></td><td><b>0.24 ± 0.10 mm</b></td><td><b>95.2%</b> (20/21)</td>
  </tr>
</table>

<table align="center">
  <tr align="center">
    <th>Clinical assessment</th><th>Without AI</th><th>With NeurAneuNet</th>
  </tr>
  <tr align="center"><td>Planning time</td><td>672 ± 225 s</td><td><b>371 ± 51 s</b></td></tr>
  <tr align="center"><td>NASA-TLX workload</td><td>33 ± 8</td><td><b>21 ± 5</b></td></tr>
  <tr align="center"><td>PED agreement</td><td>83.3%</td><td><b>96.0%</b></td></tr>
</table>

### Clinical workflow

The system follows a single clinical chain from 3DRA reconstruction and aneurysm delineation to vascular measurement, PED sizing, and physician assessment. This design keeps anatomical perception and treatment planning within the same auditable workflow.

Model development used 600 aneurysms, including a 210-case PED-treated subset with patient-level training, validation, and test partitions. Clinical utility was assessed separately in 21 cases reviewed by six neurointerventional physicians, allowing technical performance and its effect on planning behavior to be examined as distinct but connected outcomes.

<p align="center">
  <img src="assets/clinical-workflow.png" alt="NeurAneuNet clinical workflow and evaluation design"><br>
  <sub>Figure 1. Clinical workflow and PED recommendation study design.</sub>
</p>

### Representative segmentations

Representative cases compare raw angiography, expert annotations, and model predictions in both 2D slices and 3D reconstructions. The examples illustrate preservation of the aneurysm boundary and its relationship to the parent vessel across different morphologies.

Across the test set, the model achieved an overall Dice coefficient of 0.874 ± 0.03, with an HD95 of 4.5 ± 1.6 mm, sensitivity of 92.5%, and specificity of 97.8%. Performance was lower for micro and small aneurysms, as expected from their limited voxel support, but the qualitative cases show that the system continued to recover clinically relevant aneurysm-neck and parent-vessel geometry.

<p align="center">
  <img src="assets/qualitative-segmentation.png" alt="Representative 2D and 3D aneurysm segmentation cases"><br>
  <sub>Figure 2. Qualitative aneurysm segmentation in representative clinical cases.</sub>
</p>

### Segmentation and device planning

Quantitative evaluation connects segmentation quality with downstream PED selection and positioning. Performance is reported across device sizes and landing-zone targets rather than treating segmentation as an isolated endpoint.

Mean PED size-classification accuracy reached 91.8%, while diameter prediction error was 0.24 ± 0.10 mm. The mean proximal and distal landing-zone offsets were 1.52 ± 0.47 mm and 2.38 ± 0.69 mm, respectively. These results show how errors propagate from anatomical reconstruction into the device-planning variables that determine whether a recommendation is operationally useful.

<p align="center">
  <img src="assets/results-segmentation.png" alt="Published NeurAneuNet segmentation and device-planning results"><br>
  <sub>Figure 3. Segmentation and device-planning performance.</sub>
</p>

### Clinical thresholds

ROC analysis evaluates PED model discrimination, while the threshold panel summarizes whether each output meets its predefined clinical target. The combined view makes both predictive accuracy and operational acceptability visible.

The mean AUC across PED models was 95.14%, with the most common device classes reaching AUCs between 95.99% and 97.06%. Clinical-threshold achievement ranged from 89.7% for distal landing-zone deviation to 97.5% for diameter error. In the physician study, AI assistance reduced mean planning time from 672 to 371 seconds, lowered NASA-TLX workload from 33 to 21, and increased agreement with the optimal PED choice from 83.3% to 96.0%.

<p align="center">
  <img src="assets/results-clinical.png" alt="Published NeurAneuNet ROC and clinical threshold results"><br>
  <sub>Figure 4. PED classification and clinical-threshold analysis.</sub>
</p>

Published tables: [clinical assistance](results/clinical_assistance.csv) · [morphometric agreement](results/morphometric_agreement.csv) · [single vs. multiple aneurysms](results/single_vs_multiple_aneurysms.csv)

## Evaluation design and interpretation

### Anatomical validation

Segmentation is assessed with complementary volumetric and surface metrics because overlap alone cannot establish whether the reconstructed vessel is suitable for measurement. Dice summarizes overall agreement; HD95 and mean surface distance capture boundary displacement; sensitivity and specificity characterize foreground recovery and background rejection. Morphometric agreement then tests whether the predicted surface preserves quantities used in planning, including maximum diameter, neck width, neck-to-dome ratio, and aspect ratio.

The reported overall Dice of 0.874 ± 0.03 is accompanied by an HD95 of 4.5 ± 1.6 mm, a mean surface distance of 0.52 ± 0.15 mm, sensitivity of 92.5%, and specificity of 97.8%. Performance is lower for lesions below 5 mm, where partial-volume effects and limited voxel support make small absolute boundary shifts proportionally large. This size-stratified behavior is more informative than a single aggregate value because device selection may change near narrow diameter thresholds.

### Planning validation

Device planning is evaluated separately for class selection, continuous dimension estimation, and placement. The mean classification accuracy of 91.8% describes exact model selection across the evaluated PED catalogue. Diameter error of 0.24 ± 0.10 mm measures the continuous sizing problem, while length errors are reported by device-length group. Proximal and distal landing-zone offsets quantify how far the proposed deployment limits fall from their references.

The asymmetry between proximal and distal offsets is clinically interpretable. Distal placement is more sensitive to vessel curvature, tapering, and the longer anatomical path traversed by large devices. Longer and larger-diameter PEDs are also more likely to be used in anatomically complex cases, so their error distribution reflects both device properties and case difficulty. For this reason, the repository presents the component outcomes rather than reducing the planning task to one headline accuracy.

### Physician-assistance study

The independent assessment included 21 PED-treated cases and six neurointerventional physicians spanning senior, intermediate, and junior experience levels. Each physician completed planning under conventional and AI-assisted conditions, with randomized condition order and a washout interval. Outcomes included completion time, NASA-TLX workload, and agreement with an expert-defined reference device.

The aggregate results show a reduction in mean planning time from 672 ± 225 seconds to 371 ± 51 seconds, a decrease in NASA-TLX from 33 ± 8 to 21 ± 5, and an increase in device agreement from 83.3% to 96.0%. These findings describe performance within the reported controlled study. They do not establish improved procedural safety, aneurysm occlusion, or long-term patient outcomes, none of which were directly evaluated.

### Failure structure

The principal reported failure groups are complex morphology, indistinct aneurysm boundaries, and microaneurysms. These categories map to different parts of the system. Tortuosity and bifurcation proximity can destabilize centerline and landing-zone estimation; weak contrast affects neck localization; very small lesions magnify voxel-level errors; and multiple aneurysms can create competing segmentation signals. A case may therefore have an acceptable global mask while still containing a local geometric error relevant to device placement.

The failure analysis motivates a review strategy based on both confidence and anatomy. Cases with small margins between device candidates, predictions near a size transition, low-confidence recommendations, marked tortuosity, or poorly defined boundaries should receive mandatory expert inspection. The confidence signal is a triage aid for review intensity, not a guarantee of correctness.

## Research contribution

NeurAneuNet contributes a complete image-to-plan formulation rather than an isolated segmentation model. Its main technical contribution is the explicit connection between vascular perception, physical geometry, structured knowledge, and device-specific prediction. This connection makes it possible to examine how anatomical error propagates into treatment-planning error and to evaluate the system using both computational metrics and physician workflow outcomes.

The work also illustrates why multimodal fusion is valuable in interventional planning. Image features dominate local appearance, geometric descriptors encode the vessel surface in procedural units, and knowledge features become increasingly relevant when anatomy is unusual. The tensor-decomposition mechanism is designed to preserve these interactions without requiring every modality to contribute equally in every case.

Finally, the project treats clinical assistance as a separate layer of evidence. Technical accuracy, agreement with an expert reference, reduced planning time, and lower workload answer different questions. Reporting them separately avoids treating a strong segmentation score as proof of clinical effectiveness.

## Scope and limitations

The current evidence is retrospective and institutionally concentrated. Broader applicability across hospitals, scanner protocols, patient populations, and interventional practice patterns requires multicenter prospective evaluation. Rare anatomical subgroups remain small, and the present device catalogue is limited to the PED families represented in the study. Transfer to other flow-diverter brands would require new data and device-specific validation.

The system does not currently model hemodynamic change, post-deployment wall apposition, endothelial remodeling, thromboembolic events, or long-term occlusion. Consequently, the repository should be read as evidence for preoperative segmentation and planning assistance, not as evidence for procedural safety or patient-outcome benefit. The public release also excludes patient data, complete training code, model checkpoints, and institution-specific workflow assets.

## Codebase blueprint

```text
NeurAneuNet/
├── assets/                         # graphical abstract, architecture, result figures
├── results/                        # machine-readable published tables
├── configs/
│   ├── data/                       # cohort and preprocessing profiles
│   ├── model/                      # module-level model settings
│   └── experiment/                 # training and ablation protocols
├── data/
│   ├── raw/                        # local-only source data
│   ├── processed/                  # normalized volumes and derived geometry
│   └── splits/                     # patient-level split manifests
├── neuraneunet/
│   ├── datasets/                   # 3DRA loaders and transforms
│   ├── models/
│   │   ├── segmentation/           # dual-path attention U-Net++
│   │   ├── geometry/               # centerline and morphometry modules
│   │   ├── knowledge/              # vascular and device priors
│   │   ├── fusion/                 # tensor-decomposition fusion
│   │   └── decision/               # PED and landing-zone heads
│   ├── pipelines/                  # training and inference orchestration
│   ├── evaluation/                 # segmentation, planning, clinical metrics
│   └── utils/                      # reproducibility and IO utilities
├── scripts/                        # future command-line entry points
├── tests/
│   ├── unit/
│   └── integration/
└── README.md
```

The repository now includes a dependency-light public utility layer for validated data contracts, segmentation and planning metrics, and physical-space centerline geometry, with unit tests and CI. The trained multimodal model, checkpoints, and clinical data are not included in this release.

<details>
<summary><b>Citation</b></summary>

```bibtex
@article{wen2026neuranunet,
  title   = {Multimodal Deep Learning and Knowledge-Enhanced Intelligent Decision Support System for Pipeline Embolization Device Size Selection in Intracranial Aneurysm Treatment},
  author  = {Wen, Zhihong and Guo, Shengli and Peng, Yulin and Chen, Yakun and Huangfu, Luokai and Zhao, Hao and Gao, Hao and Ni, Taoyi and Zhang, Jianning and Liu, Xiangpeng and Liu, Jiayu and Liang, Yongping},
  journal = {CNS Neuroscience \& Therapeutics},
  volume  = {32},
  number  = {7},
  pages   = {e71047},
  year    = {2026},
  doi     = {10.1002/cns.71047}
}
```

</details>
