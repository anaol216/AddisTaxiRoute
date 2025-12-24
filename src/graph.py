import json

class Graph:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.adj = json.load(f)

    def neighbors(self, node):
        return self.adj.get(node, {})
