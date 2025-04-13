# VLSI Partitioning Using Classical ML Techniques

This repository contains the codebase for our CSL2050: Pattern Recognition and Machine Learning course project at IIT Jodhpur. Our objective is to apply classical machine learning techniques to the problem of VLSI netlist partitioning.

## 🧠 Problem Overview

In modern VLSI design, a circuit is represented as a netlist graph, where:

- **Nodes** represent gates/components with attributes like power and area
- **Edges** represent wires between components with attributes like distance and wires

The goal is to partition the netlist into balanced components while minimizing:

- ✂️ Cut edges (inter-partition connections)
- 🔌 Total wire length
- ⏱️ Critical path delay
- ⚡ Power consumption imbalance
- 📐 Area imbalance

## 📁 Project Structure:
PRML_25_proj/
├── Analysis/
├── Dataset/
├── Models/
│ ├── Agglomerative_model.py
│ ├── Kmeans_1d.py
│ ├── Logistic_model.py
│ └── SVM_model.py
├── Pre-Processing/
├── utils/
│ ├── crit_path.py
│ └── graph_gen.py
├── app.py
├── README.md
└── requirements.txt


## 🧪 Implemented Models

| Model                     | Type          | Description |
|---------------------------|---------------|-------------|
| `Kmeans_1d.py`            | Unsupervised  | Clusters 1D projected features (distance-based) |
| `Agglomerative_model.py`  | Unsupervised  | Hierarchical clustering with power/area features |
| `SVM_model.py`            | Supervised    | Trained on pseudo-labels from KMeans |
| `Logistic_model.py`       | Supervised    | Probabilistic binary classifier for partitioning |

Each model returns:

- `partition_map`: Node → Cluster ID
- `cut_edges`: Number of cross-cluster connections
- `total_wire_length`: Overall wire length
- `partition_power`, `partition_area`: Stats per partition
- `silhouette_score`: Cluster compactness score

## 📊 Sample Results

| Model            | Cut Edges | Wire Length | Delay | Power Balance | Area Balance |
|------------------|-----------|-------------|-------|---------------|--------------|
| KMeans           | 22        | 151.4       | 32.9  | ⚖️ ~equal     | ⚖️ ~equal    |
| SVM              | 19        | 149.2       | 29.5  | ⚖️            | ⚖️           |
| Logistic Reg.    | 21        | 150.8       | 30.1  | ⚖️            | ⚖️           |
| Agglomerative    | 17        | 162.7       | 54.6  | ✅            | ✅           |

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/Sohom-Sarkar/PRML_25_proj.git
cd PRML_25_proj

