<div align="center">

# NeurAneuNet

**Knowledge-enhanced multimodal planning for intracranial aneurysm intervention**

[![Paper](https://img.shields.io/badge/Paper-CNS_Neuroscience_&_Therapeutics-4C78A8?style=flat-square)](https://doi.org/10.1002/cns.71047)
[![Open Access](https://img.shields.io/badge/Open_Access-CC_BY_4.0-2A9D8F?style=flat-square)](https://doi.org/10.1002/cns.71047)
[![AneuFusion](https://img.shields.io/badge/Extension-AneuFusion-8B5CF6?style=flat-square)](#architecture--aneufusion)
[![Code](https://img.shields.io/badge/Code-structure_only-6B7280?style=flat-square)](#repository-layout)

<sub>3D-DSA · geometric priors · clinical variables · PED planning</sub>

</div>

<p align="center">
  <img src="assets/graphical-abstract.png" width="920" alt="NeurAneuNet graphical abstract">
</p>

NeurAneuNet unifies vascular segmentation, anatomical knowledge, multimodal fusion, and PED sizing in one decision-support pipeline.

## Architecture · AneuFusion

AneuFusion extends the shared neurovascular backbone with dual-pathway encoding, ML-KAN feature extraction, and tensor-decomposition fusion.

<p align="center">
  <img src="assets/architecture.png" width="920" alt="AneuFusion multimodal architecture">
</p>

## Published results

| Segmentation Dice | PED classification | Diameter error | External recommendation |
|:---:|:---:|:---:|:---:|
| **0.874 ± 0.03** | **91.8%** | **0.24 ± 0.10 mm** | **95.2%** (20/21) |

### Segmentation and device planning

<p align="center">
  <img src="assets/results-segmentation.png" width="900" alt="Published NeurAneuNet segmentation and device-planning results">
</p>

### Clinical thresholds

<p align="center">
  <img src="assets/results-clinical.png" width="960" alt="Published NeurAneuNet ROC and clinical threshold results">
</p>

## Repository layout

```text
NeurAneuNet/
├── assets/                 # graphical abstract, architecture, and results
├── configs/                # experiment configurations
├── data/                   # dataset interfaces
├── models/
│   ├── segmentation/       # vascular segmentation backbone
│   ├── fusion/             # multimodal tensor fusion
│   └── decision/           # PED sizing and landing-zone heads
├── evaluation/             # model and clinical evaluation
└── README.md
```

> Model implementation is not included in this release.

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
