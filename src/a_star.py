# AddisTaxiRoute/src/a_star.py
import heapq
from .heuristics import h

def a_star(graph, start, goal):
    open_set = []
    # (f_cost, g_cost, current_node, path_list)
    heapq.heappush(open_set, (h(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path, g
        
        if current in visited:
            continue
            
        visited.add(current)

        for neighbor, cost in graph.neighbors(current).items():
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + h(neighbor, goal)
                heapq.heappush(open_set, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float('inf')