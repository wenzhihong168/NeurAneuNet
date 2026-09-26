<div align="center">

# NeurAneuNet

**Knowledge-enhanced multimodal planning for intracranial aneurysm intervention**

[![Paper](https://img.shields.io/badge/Paper-CNS_Neuroscience_&_Therapeutics-4C78A8?style=flat-square)](https://doi.org/10.1002/cns.71047)
[![Open Access](https://img.shields.io/badge/Open_Access-CC_BY_4.0-2A9D8F?style=flat-square)](https://doi.org/10.1002/cns.71047)
[![Code](https://img.shields.io/badge/Code-structure_only-6B7280?style=flat-square)](#repository-layout)

</div>

NeurAneuNet unifies 3D vascular segmentation, geometric knowledge, multimodal fusion, and PED sizing within one decision-support pipeline.

## Architecture

<p align="center">
  <img src="assets/architecture.png" width="820" alt="NeurAneuNet architecture">
</p>

## Results

| PED recommendation | Planning time | Physician agreement |
|:---:|:---:|:---:|
| **95.2%** (20/21) | **672 → 371 s** | **83.3% → 96.0%** |

<p align="center">
  <img src="assets/results.png" width="900" alt="NeurAneuNet results">
</p>

## AneuFusion

**Research extension · manuscript in preparation**

AneuFusion shares the neurovascular backbone and extends the system with structured image–geometry–clinical fusion for PED selection.

| Selection accuracy | Diameter RMSE | Parameters |
|:---:|:---:|:---:|
| **82.1%** | **0.42 mm** | **14.8 M** |

<p align="center">
  <img src="assets/aneufusion-comparison.png" width="900" alt="AneuFusion multimodal fusion comparison">
</p>

## Repository layout

```text
NeurAneuNet/
├── assets/                 # architecture and result figures
├── configs/                # experiment configurations
├── data/                   # dataset interfaces
├── models/
│   ├── segmentation/       # vascular segmentation backbone
│   ├── fusion/             # multimodal tensor fusion
│   └── decision/           # PED sizing and landing-zone heads
├── evaluation/             # clinical and model evaluation
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
