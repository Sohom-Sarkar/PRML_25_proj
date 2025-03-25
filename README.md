# PRML_25_proj

# VLSI Partitioning using Classical ML Techniques

This repository contains the codebase for our **CSL2050: Pattern Recognition and Machine Learning** course project at IIT Jodhpur. Our objective is to apply classical machine learning techniques to the problem of **VLSI netlist partitioning**.

## 🧩 Problem Overview

In modern **VLSI design**, a circuit is represented as a **netlist graph**, where:
- **Nodes** = gates/components (with `power` and `area` attributes)
- **Edges** = wires between them (with `distance`, `wires` attributes)

The goal is to **partition the netlist** into balanced components while minimizing:
- ✂️ **Cut edges** (inter-partition connections)
- 🧵 **Total wire length**
- ⏱️ **Critical path delay**
- 🔋 **Power consumption imbalance**
- 📐 **Area imbalance**

## ⚙️ Project Structure
📁 models/<br>
  |- Kmeans_1d.py<br>
  |- Agglomerative_model.py<br>
  |- SVM_model.py<br>
  -- Logistic_model.py<br>

📁 utils/<br>
 |- graph_gen.py # Graph and netlist generator<br>
 -- crit_path.py # Critical path analysis<br>

📁 notebooks/<br>
 |- Graph_Gen_1_2.ipynb<br>
 |- Crit_Path_1.ipynb<br>
 -- Kmeans_1d.ipynb<br>


## 🤖 Implemented Models

| Model                      | Type          | Key Notes |
|----------------------------|---------------|-----------|
| `KMeans_1d.py`             | Unsupervised  | Clusters 1D projected features (distance-based) |
| `Agglomerative_model.py`   | Unsupervised  | Hierarchical clustering with power/area features |
| `SVM_model.py`             | Supervised    | Trained on pseudo-labels from KMeans |
| `Logistic_model.py`        | Supervised    | Probabilistic binary classifier for partitioning |

Each model returns:
- `partition_map`: node → cluster ID
- `cut_edges`: number of cross-cluster connections
- `total_wire_length`: overall wire length
- `partition_power`, `partition_area`: stats per partition
- `silhouette_score`: cluster compactness score

## 📊 Sample Results

| Model      | Cut Edges | Wire Length | Delay | Power Balance | Area Balance |
|------------|-----------|-------------|-------|----------------|--------------|
| KMeans     | 22        | 151.4       | 32.9  | ⚖️ ~equal      | ⚖️ ~equal    |
| SVM        | 19        | 149.2       | 29.5  | ⚖️             | ⚖️           |
| LogReg     | 21        | 150.8       | 30.1  | ⚖️             | ⚖️           |
| Agglomerative | 17     | 162.7       | 54.6  | ✅             | ✅           |

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/Sohom-Sarkar/PRML_25_proj.git
cd PRML_25_proj

Install dependencies:
pip install -r requirements.txt

Generate a graph and run a model:
from utils.graph_gen import generate_netlist
from models.SVM_model import train_svm_on_graph

G, inputs, outputs = generate_netlist(num_nodes=50, num_edges=100)
results = train_svm_on_graph(G)
print(results)

🎥 Deliverables
✅ Mid-term report

✅ Classical ML model implementations

📈 Final report (in progress)

🎬 Spotlight video

🌐 Project Webpage

💾 Web/demo inference script

📜 Minutes of meetings

👥 Team
Sohom Sarkar [B23EE1099]

Rudra Khokhani

Aditya Jha

Tula Mrudhul

Sambhav Jha

🧾 License
This repository is for academic purposes under IIT Jodhpur's PRML course. All rights reserved by the authors.
