# VLSI Netlist Partitioning using Classical Machine Learning

This project explores the application of classical machine learning techniques to the partitioning of VLSI (Very Large Scale Integration) circuit netlists. We represent VLSI designs as directed graphs and aim to divide them into balanced and efficient subgraphs while minimizing key metrics including:

- **Number of interconnections (cut size)**
- **Total wire length**
- **Critical path delay**

Our approach evaluates multiple models, including unsupervised clustering techniques (KMeans, Agglomerative Clustering, Spectral Clustering) and supervised classification methods (SVM, Logistic Regression) applied to synthetic circuit graphs.

---

## 🚀 Features

- **Synthetic Graph Generator**: Creates realistic VLSI netlist representations with configurable parameters
- **Multiple Partitioning Models**: Implements and compares 5 different ML techniques
- **Comprehensive Evaluation**: Analyzes model performance across various graph sizes and densities
- **Interactive Visualization**: Includes Streamlit app for real-time exploration and comparison
- **Extensible Framework**: Easily add new models and evaluation metrics

---

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/vlsi-ml-partitioning.git
cd vlsi-ml-partitioning
```
```bash
# Create and activate virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
```bash
# Install dependencies
pip install -r requirements.txt
```

# Quick Start
```python
from src.graph_generator import NetlistGenerator
from src.models import SpectralClustering, KMeansClustering
from src.evaluation import evaluate_partition

# Generate a synthetic netlist
generator = NetlistGenerator(nodes=100, edge_factor=1.5)
graph = generator.generate()

# Apply spectral clustering
model = SpectralClustering(alpha=0.5, n_clusters=2)
partition = model.fit_predict(graph)

# Evaluate the partitioning
metrics = evaluate_partition(graph, partition)
print(f"Cut size: {metrics['cut_size']}")
print(f"Delay: {metrics['delay']}")
print(f"Wire length: {metrics['wire_length']}")
```

# Running the Streamlit App
```bash
streamlit run app.py
```

# Project Structure

vlsi-ml-partitioning/
├── data/                  # Sample graph datasets and benchmarks
├── notebooks/             # Jupyter notebooks for analysis and visualization
├── src/                   # Source code
│   ├── graph_generator.py # Graph generation module
│   ├── models/            # ML models implementation
│   ├── evaluation.py      # Metrics and evaluation functions
│   └── utils.py           # Helper functions
├── app.py                 # Streamlit application
├── requirements.txt       # Dependencies
└── README.md              # This file

# Implemented Models

1. KMeans Clustering (1D)
- Strengths: Fast convergence, computational efficiency, interpretable
- Limitations: Sensitive to initial centroid selection, requires predefined number of clusters (k)

2. Agglomerative Clustering
- Strengths: Hierarchical visualization, doesn’t require predefined cluster count, works well for certain topologies
- Limitations: Performance depends heavily on graph structure

3. Support Vector Machines (SVM)
- Strengths: Handles non-linear separation via kernels, robust to outliers
- Limitations: Less interpretable with non-linear kernels, requires tuning

4. Logistic Regression
- Strengths: Fast, efficient, interpretable coefficients
- Limitations: Assumes linearly separable classes, sensitive to noise

5. Spectral Clustering
- Strengths: Captures non-convex clusters, leverages global graph structure
- Limitations: Computationally expensive, sensitive to hyperparameters
