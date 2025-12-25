# AddisTaxiRoute/src/graph.py
import json

class Graph:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Initialize the adjacency list to store the final, bidirectional graph
        self.adj = {}
        
        # Build the graph, ensuring every connection is bidirectional (undirected)
        for u, neighbors in data.items():
            # Ensure the source node 'u' is in the adjacency list
            if u not in self.adj:
                self.adj[u] = {}
                
            for v, cost in neighbors.items():
                # --- 1. Add the forward edge u -> v ---
                self.adj[u][v] = cost
                
                # --- 2. Add the reverse edge v -> u to make it undirected ---
                # Ensure the destination node 'v' is in the adjacency list
                if v not in self.adj:
                    self.adj[v] = {}
                
                # Add the reverse connection with the same cost
                self.adj[v][u] = cost 

    def neighbors(self, node):
        return self.adj.get(node, {})