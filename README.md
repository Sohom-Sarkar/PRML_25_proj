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
- Analysis/
- Dataset/
- Models/
-- Agglomerative_model.py
-- Kmeans_1d.py
-- Logistic_model.py
-- SVM_model.py
- Pre-Processing/
- utils/
-- crit_path.py
-- graph_gen.py
- app.py
- README.md
- requirements.txt


## 🧪 Implemented Models

| Model                     | Type          | Description |
|---------------------------|---------------|-------------|
| `Kmeans_1d.py`            | Unsupervised  | Clusters 1D projected features (distance-based) |
| `Agglomerative_model.py`  | Unsupervised  | Hierarchical clustering with power/area features |
| `SVM_model.py`            | Supervised    | Trained on pseudo-labels from KMeans |
| `Logistic_model.py`       | Supervised    | Probabilistic binary classifier for partitioning |
| `Spectral_cl.py`          | Unsupervised  | Uses affinity matrix (exp(-awires+bdist)) and Spectral Clustering algorithm. |

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
| Spectral         | 43        | 2748.7      | 634.4 | ✅            | ✅           |

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/Sohom-Sarkar/PRML_25_proj.git
cd PRML_25_proj
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Generate a graph and run a model:
```bash
from utils.graph_gen import generate_netlist
from Models.SVM_model import train_svm_on_graph

G, inputs, outputs = generate_netlist(num_nodes=50, num_edges=100)
results = train_svm_on_graph(G)
print(results)
```

📄 Deliverables:

- Mid-term report

- Classical ML model implementations

- Final report (in progress)

- Spotlight video

- Project webpage

- Web/demo inference script

- Minutes of meetings

👥 Team:

- Sohom Sarkar [B23EE1099]

- Rudra Khokhani

- Aditya Jha

- Tula Mrudhul

- Sambhav Jha

📜 License
This repository is for academic purposes under IIT Jodhpur's PRML course. All rights reserved by the authors.



