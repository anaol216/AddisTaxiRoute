# app.py (Updated with UI and Robust Graphing)
import os
import sys

# Adjust path to import modules from the src directory
# This assumes the app.py is run from the root directory of the project
sys.path.append(os.path.abspath("./src")) 

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Import custom classes/functions
try:
    from src.graph import Graph
    from src.a_star import a_star
    from src.heuristics import h, heuristic # Import heuristic table and function
except ImportError as e:
    st.error(f"Error loading project modules: {e}. Ensure src/graph.py and src/a_star.py exist.")
    st.stop() # Stop the app if core modules are missing

## --- 1. CONFIGURATION AND DATA LOADING ---
# Set the page configuration for a wider layout
st.set_page_config(layout="wide")

# Load graph
try:
    graph = Graph("data/stations.json")
    stations = list(graph.adj.keys())
except FileNotFoundError:
    st.error("Error: data/stations.json not found. Check your file path.")
    st.stop()
    
## --- 2. STREAMLIT UI LAYOUT ---

# Header with image
col1, col2 = st.columns([1, 4])

with col1:
    # Add a cool city image (Replace with an actual image link or local file path)
    # 
    st.image("https://plus.unsplash.com/premium_photo-1697729902269-70f031f22531?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
             width=150) 
with col2:
    st.title("🇪🇹 Addis Ababa Taxi Route Finder")
    st.markdown("### Optimal Routing powered by **A\* Search**")

st.markdown("---")

# Main selection interface
col3, col4, col5 = st.columns(3)

with col3:
    start_station = st.selectbox("🚦 Start Station", stations, key="start")

with col4:
    end_station = st.selectbox("🏁 Goal Station", stations, key="goal")

with col5:
    # Add a clear button for finding the route
    st.markdown("<br>", unsafe_allow_html=True) # Adds vertical space
    if st.button("Find Optimal Route", type="primary", use_container_width=True):
        st.session_state['run_search'] = True
    else:
        # Initialize or reset search state
        if 'run_search' not in st.session_state:
            st.session_state['run_search'] = False

st.markdown("---")

## --- 3. ALGORITHM EXECUTION AND RESULTS DISPLAY ---

if st.session_state.get('run_search', False):
    
    # Run the A* algorithm
    path, cost = a_star(graph, start_station, end_station)
    
    # Display Cost and Path
    result_col1, result_col2 = st.columns(2)

    with result_col1:
        if path:
            st.success(f"✅ Optimal Path Found!")
            st.metric(label="Total Minimum Travel Time (Cost)", value=f"{cost} minutes")
            
            # Additional cool feature: Display the heuristic used for the goal
            if end_station in heuristic:
                st.markdown(f"> *Heuristic H({end_station}): {h(end_station)} minutes*")
        else:
            st.error("No path found!")
            
    with result_col2:
        if path:
            st.info(f"Route: {' → '.join(path)}")
            
    st.markdown("---")
    
    ## --- 4. VISUALIZATION ---
    if path:
        
        st.subheader("🗺️ Optimal Route Visualization")
        
        # --- ROBUST NETWORKX GRAPH CREATION (The Critical Fix) ---
        # Create a new graph G by explicitly defining the 'weight' attribute 
        # to ensure the drawing functions work correctly without KeyError/StopIteration.
        G = nx.Graph()
        added_edges = set() 
        for u, neighbors in graph.adj.items():
            for v, cost_val in neighbors.items():
                if (v, u) not in added_edges:
                    G.add_edge(u, v, weight=cost_val)
                    added_edges.add((u, v))
        
        # Use a fixed position for consistency
        pos = nx.spring_layout(G, seed=42)

        plt.figure(figsize=(12, 8))
        
        # Highlight path elements
        path_nodes = set(path)
        path_edges = list(zip(path, path[1:]))

        # 1. Draw all edges (base map)
        nx.draw_networkx_edges(G, pos, edge_color="lightgray", width=0.5)
        
        # 2. Draw all nodes
        node_colors = []
        for node in G.nodes():
            if node == start_station:
                node_colors.append("green")
            elif node == end_station:
                node_colors.append("red")
            elif node in path_nodes:
                node_colors.append("gold")
            else:
                node_colors.append("skyblue")
                
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=2500)
        
        # 3. Draw labels with heuristic (Cool Feature)
        node_labels = {node: f"{node}\n(h={h(node, end_station)})" for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=9, font_weight="bold")
        
        # 4. Draw path edges brightly
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=4, style='solid')
        
        # 5. Draw edge weights (using the guaranteed 'weight' attribute)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue', font_size=10)
        
        plt.title(f"Optimal Path: {start_station} → {end_station}", fontsize=16)
        plt.axis('off')
        st.pyplot(plt)

    # Reset search state after display
    st.session_state['run_search'] = False