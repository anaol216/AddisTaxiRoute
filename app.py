# app.py (or whatever you call your main file)
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
        G = nx.Graph(graph.adj) # This now uses the fully connected, undirected graph
        
        # Use a fixed position for consistency
        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(10,6))
        # Draw all nodes and edges
        nx.draw_networkx_nodes(G, pos, node_color="skyblue", node_size=2000)
        nx.draw_networkx_labels(G, pos, font_size=10)
        
        # Draw edge weights
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        
        # Highlight path
        edge_path = list(zip(path, path[1:]))
        
        # Create a list of all edges in the graph
        all_edges = G.edges()
        
        # Separate path edges from non-path edges for drawing
        non_path_edges = [edge for edge in all_edges if edge not in edge_path and (edge[1], edge[0]) not in edge_path]
        
        # Draw non-path edges in a lighter color
        nx.draw_networkx_edges(G, pos, edgelist=non_path_edges, edge_color="gray", width=1)
        
        # Draw path edges in a bright color and thick line
        nx.draw_networkx_edges(G, pos, edgelist=edge_path, edge_color="green", width=3, style='dashed')
        
        # Highlight path nodes
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="orange", node_size=2000)
        
        st.pyplot(plt)
    else:
        st.error("No path found!")