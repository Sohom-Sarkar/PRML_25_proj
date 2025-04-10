# Streamlit-based Interactive Web Demo for VLSI Partitioning

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from models.Kmeans_1d import train_kmeans_on_graph  # Replace with any model you want
from utils.graph_gen import generate_netlist

st.set_page_config(page_title="VLSI Partitioning Demo", layout="wide")
st.title("🔧 Interactive VLSI Partitioning Demo")

# Sidebar controls
st.sidebar.header("Graph Parameters")
num_nodes = st.sidebar.slider("Number of Nodes", min_value=10, max_value=100, value=50)
num_edges = st.sidebar.slider("Number of Edges", min_value=20, max_value=300, value=100)

st.sidebar.header("Graph Settings")
enable_power = st.sidebar.checkbox("Enable Power Attribute", value=True)
enable_area = st.sidebar.checkbox("Enable Area Attribute", value=True)
enable_distance = st.sidebar.checkbox("Enable Edge Distance", value=True)
enable_wire_count = st.sidebar.checkbox("Enable Wire Count", value=True)

# Generate graph
if st.sidebar.button("Generate Graph & Partition"):
    G, inputs, outputs = generate_netlist(
        num_nodes=num_nodes,
        num_edges=num_edges,
        enable_power=enable_power,
        enable_area=enable_area,
        enable_distance=enable_distance,
        enable_wire_count=enable_wire_count
    )

    results = train_kmeans_on_graph(G)  # Change this line to switch model

    partition_map = results["partition_map"]
    colors = [partition_map.get(n, -1) for n in G.nodes()]

    st.subheader("📊 Partitioned Graph")
    fig, ax = plt.subplots(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color=colors, cmap=plt.cm.Set2, ax=ax)
    st.pyplot(fig)

    st.subheader("📈 Metrics")
    st.json({
        "Cut Edges": results["cut_edges"],
        "Total Wire Length": results["total_wire_length"],
        "Power per Partition": results["partition_power"],
        "Area per Partition": results["partition_area"]
    })

    st.success("Done!")

else:
    st.info("Adjust parameters on the left and click 'Generate Graph & Partition' to begin.")
