# system imports
import os
import sys

sys.path.append(os.path.abspath("./src"))

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from src.graph import Graph
from src.a_star import a_star

# Load graph
graph = Graph("data/stations.json")
stations = list(graph.adj.keys())

st.title("Addis Ababa Taxi Route Finder")
st.write("Select start and end stations:")

start_station = st.selectbox("Start Station", stations)
end_station = st.selectbox("Goal Station", stations)

if st.button("Find Optimal Route"):
    path, cost = a_star(graph, start_station, end_station)
    if path:
        st.success(f"Optimal Path: {' -> '.join(path)}")
        st.info(f"Total Cost (Distance/Time): {cost}")

        # Draw graph
        G = nx.Graph(graph.adj)
        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(10,6))
        nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=10)
        # Highlight path
        edge_path = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color="orange", width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="orange", node_size=2000)
        st.pyplot(plt)
    else:
        st.error("No path found!")
