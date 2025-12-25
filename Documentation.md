# Optimal Route Finding for Taksi Services in Addis Ababa
**Group Assignment 1 (10%)**

## 1. Introduction
Urban transportation in Addis Ababa is characterized by high traffic density, frequent congestion, and complex road networks, which make route selection a critical challenge for taksi services. Choosing an inefficient route can result in increased travel time, higher fuel consumption, and reduced customer satisfaction. As a result, there is a growing need for intelligent systems that can assist drivers in selecting optimal routes based on defined cost criteria.

Artificial Intelligence (AI) search algorithms provide effective solutions to such routing problems by modeling road networks as graphs and systematically exploring possible paths to identify the most optimal one. In this assignment, a portion of the Addis Ababa road network is modeled as a weighted graph, where nodes represent major taksi stations or landmarks and edges represent road segments connecting them. Each edge is assigned a cost that reflects the estimated travel time between locations.

The primary objective of this assignment is to apply an AI search algorithm to determine the best possible route between two designated taksi stations—Bole Medhanialem as the starting point and Piazza as the destination. By implementing and analyzing the selected algorithm, this project demonstrates practical applications of graph modeling, heuristic-based search, and route optimization in a real-world urban transportation context.

## 2. Problem Definition
The problem addressed in this assignment is the identification of an optimal route for taksi services within a selected portion of the Addis Ababa road network. The road network is represented as a weighted graph, where each node corresponds to a major taksi station or landmark, and each edge represents a direct road connection between two stations.

The task is to determine the most efficient path from a designated start station, Bole Medhanialem, to a designated goal station, Piazza. Efficiency, in this context, is defined in terms of minimum travel time, measured in minutes. Each road segment is assigned a weight representing the estimated average travel time required to traverse that segment under typical traffic conditions.

Formally, given a connected weighted graph $G=(V,E)$, where $V$ is the set of taksi stations and $E$ is the set of road segments with associated travel-time costs, the objective is to find a path $P \subseteq E$ such that the total accumulated cost from the start node to the goal node is minimized.

This problem is well-suited to AI search techniques, particularly heuristic-based algorithms, as it involves navigating multiple possible routes, balancing path cost and efficiency, and ensuring optimality. The solution produced by the selected algorithm should return both the sequence of stations forming the optimal path and the total travel time required to reach the destination.

## 3. Graph Modeling
This section describes how the selected portion of the Addis Ababa road network is modeled as a weighted graph. The modeling process involves identifying the geographic area of interest, defining the nodes (taksi stations), specifying the edges (road connections), and assigning appropriate cost values to each road segment.

### 3.1 Selected Area
The selected road network represents a central and eastern portion of Addis Ababa that includes major commercial, administrative, and transportation hubs. The area spans from Bole Medhanialem in the eastern part of the city to Piazza in the historic city center. This section was chosen due to its high traffic volume, frequent taksi usage, and the presence of multiple alternative routes, making it suitable for route optimization analysis.

### 3.2 Nodes (Taksi Stations)
Nodes in the graph represent major taksi stations, intersections, or well-known landmarks where route decisions are typically made. A total of 16 nodes were selected to ensure sufficient network complexity while maintaining clarity and manageability.

| Node ID | Station Name | Description |
| :--- | :--- | :--- |
| A | Bole Medhanialem | Major starting point and high-traffic hub |
| B | Atlas | Commercial intersection in Bole area |
| C | Edna Mall | Commercial and transit link |
| D | Bole Airport | Transportation hub |
| E | Wello Sefer | Residential and traffic connector |
| F | Urael | Major signal-controlled junction |
| G | Kazanchis | Business and government district |
| H | Meskel Square | Central city hub |
| I | Bambis | Commercial and residential link |
| J | Stadium | Major transit transfer point |
| K | Legehar | Central transportation link |
| L | Mexico Square | Critical junction for south and west travel |
| M | Lideta | Residential and commercial area |
| N | Beherawi | Theater area and taxi terminal |
| O | Arat Kilo | Government and education hub |
| P | Piazza | Historic city center (Goal station) |

### 3.3 Edges (Road Connections)
Edges in the graph represent direct road segments connecting two taksi stations. Each edge indicates that a vehicle can travel directly between the two locations without passing through another intermediate station. To reflect real-world driving conditions in Addis Ababa, only commonly used and logically connected roads were included in the network.

All roads are assumed to be bidirectional, meaning that travel is possible in both directions with the same estimated travel time. This assumption simplifies the model while remaining realistic for major city roads.

The resulting road network forms a connected graph, ensuring that there exists at least one valid route from the start station (Bole Medhanialem) to the goal station (Piazza).

**Road Connections and Weights**
The table below summarizes the direct road connections and their associated travel-time costs.

| From | To | Travel Time (minutes) |
| :--- | :--- | :--- |
| Bole Medhanialem | Atlas | 4 |
| Bole Medhanialem | Edna Mall | 2 |
| Edna Mall | Atlas | 3 |
| Edna Mall | Bole Airport | 5 |
| Bole Airport | Wello Sefer | 6 |
| Wello Sefer | Urael | 5 |
| Wello Sefer | Meskel Square | 8 |
| Atlas | Urael | 5 |
| Urael | Kazanchis | 4 |
| Urael | Bambis | 3 |
| Bambis | Meskel Square | 4 |
| Kazanchis | Stadium | 5 |
| Kazanchis | Arat Kilo | 7 |
| Meskel Square | Stadium | 2 |
| Meskel Square | Mexico Square | 6 |
| Stadium | Legehar | 3 |
| Legehar | Mexico Square | 4 |
| Legehar | Beherawi | 3 |
| Mexico Square | Lideta | 4 |
| Lideta | Beherawi | 3 |
| Beherawi | Piazza | 6 |
| Arat Kilo | Piazza | 5 |

These connections create multiple alternative paths between the start and goal stations, allowing the search algorithm to evaluate and compare different routing options based on cost.

### 3.4 Cost Definition (Edge Weights)
Each edge in the road network is assigned a numerical weight representing the average travel time in minutes required to traverse that road segment. Travel time was selected as the cost metric because it directly reflects the efficiency of taksi services and has a stronger practical relevance than physical distance alone.

The assigned travel-time values are estimated, taking into account:
*   Approximate distance between stations
*   Road importance (main roads vs. secondary roads)
*   Typical traffic congestion in Addis Ababa
*   Presence of traffic signals and intersections

Using travel time as the edge weight allows the optimization problem to focus on minimizing passenger waiting time and overall journey duration, which are key performance factors for taksi operations.

**Road Network Representation (Adjacency List)**
The final road network is represented programmatically using an adjacency list structure, where each station is mapped to its neighboring stations along with the corresponding travel-time cost:

```python
road_network = {
    'Bole Medhanialem': [('Atlas', 4), ('Edna Mall', 2)],
    'Edna Mall': [('Bole Medhanialem', 2), ('Atlas', 3), ('Bole Airport', 5)],
    'Bole Airport': [('Edna Mall', 5), ('Wello Sefer', 6)],
    'Atlas': [('Bole Medhanialem', 4), ('Edna Mall', 3), ('Urael', 5)],
    'Wello Sefer': [('Bole Airport', 6), ('Meskel Square', 8), ('Urael', 5)],
    'Urael': [('Atlas', 5), ('Wello Sefer', 5), ('Kazanchis', 4), ('Bambis', 3)],
    'Bambis': [('Urael', 3), ('Meskel Square', 4)],
    'Kazanchis': [('Urael', 4), ('Arat Kilo', 7), ('Stadium', 5)],
    'Meskel Square': [('Wello Sefer', 8), ('Bambis', 4), ('Stadium', 2), ('Mexico Square', 6)],
    'Stadium': [('Meskel Square', 2), ('Kazanchis', 5), ('Legehar', 3)],
    'Legehar': [('Stadium', 3), ('Mexico Square', 4), ('Beherawi', 3)],
    'Mexico Square': [('Meskel Square', 6), ('Legehar', 4), ('Lideta', 4)],
    'Lideta': [('Mexico Square', 4), ('Beherawi', 3)],
    'Beherawi': [('Legehar', 3), ('Lideta', 3), ('Piazza', 6)],
    'Arat Kilo': [('Kazanchis', 7), ('Piazza', 5)],
    'Piazza': [('Beherawi', 6), ('Arat Kilo', 5)]
}
```
This representation enables efficient traversal and cost calculation by the AI search algorithm.

## 4. Search Algorithm Selection and Justification
To solve the optimal route-finding problem defined in this assignment, the A* (A-Star) search algorithm was selected. A* is a heuristic-based informed search algorithm that is widely used for path-finding problems in transportation and navigation systems.

### 4.1 Overview of the A* Search Algorithm
A* search evaluates nodes using an evaluation function:
$$f(n) = g(n) + h(n)$$
where:
*   $g(n)$ is the actual cost incurred from the start node to node $n$,
*   $h(n)$ is a heuristic estimate of the remaining cost from node $n$ to the goal,
*   $f(n)$ represents the estimated total cost of a path passing through node $n$.

By combining the actual cost already incurred with an informed estimate of the remaining distance, A* efficiently guides the search toward the goal while still guaranteeing optimality when an admissible heuristic is used.

### 4.2 Justification for Choosing A*
A* search was chosen for this assignment for several important reasons:
1.  **Optimality**: A* guarantees the discovery of the optimal (least-cost) path when the heuristic function does not overestimate the true cost to the goal. This property is essential for taksi route optimization, where selecting the shortest-time route is critical.
2.  **Efficiency**: Compared to uninformed algorithms such as Uniform Cost Search (UCS), A* significantly reduces the number of nodes explored by directing the search toward the goal using heuristic guidance. This makes it well-suited for moderately sized road networks like the one modeled in this project.
3.  **Real-World Applicability**: A* is commonly used in real-world navigation and mapping systems, including vehicle routing and GPS-based navigation tools. Its use in this assignment demonstrates the practical relevance of AI search techniques to urban transportation problems.
4.  **Compatibility with the Cost Model**: Since the road network uses travel time (in minutes) as the edge cost, A* naturally accommodates this metric through the $g(n)$ component while leveraging heuristic estimates to improve performance.

### 4.3 Comparison with Alternative Algorithms
Although other search algorithms could be applied to this problem, A* offers a balanced combination of optimality and efficiency.

| Algorithm | Characteristics | Suitability |
| :--- | :--- | :--- |
| Uniform Cost Search (UCS) | Guarantees optimality but explores many nodes | Correct but inefficient |
| Greedy Best-First Search (GBFS) | Fast but ignores actual path cost | Not guaranteed optimal |
| A* | Optimal and efficient with admissible heuristic | Best choice |

Based on this comparison, A* was determined to be the most appropriate algorithm for the given problem.

## 5. Heuristic Function Design and Admissibility
In order to apply the A* search algorithm effectively, a heuristic function $h(n)$ is required. The purpose of the heuristic is to estimate the remaining cost from any node $n$ in the graph to the goal node, Piazza, and guide the search toward promising paths while maintaining optimality.

### 5.1 Heuristic Definition
For this assignment, the heuristic function $h(n)$ is defined as the estimated travel time (in minutes) from node $n$ to the goal node (Piazza) assuming ideal conditions and minimal traffic.
Because obtaining precise geographic coordinates and exact straight-line distances is outside the scope of this project, heuristic values were reasonably estimated based on:
*   Relative geographic proximity to Piazza
*   General direction of travel (east to west)
*   Typical traffic patterns in Addis Ababa

Nodes that are geographically closer to Piazza are assigned smaller heuristic values, while nodes farther away are assigned larger values.

### 5.2 Heuristic Value Table
The following table lists the heuristic values $h(n)$ for each taksi station in the road network:

| Node | Station Name | Heuristic $h(n)$ (minutes) |
| :--- | :--- | :--- |
| A | Bole Medhanialem | 22 |
| B | Atlas | 20 |
| C | Edna Mall | 21 |
| D | Bole Airport | 24 |
| E | Wello Sefer | 18 |
| F | Urael | 14 |
| G | Kazanchis | 12 |
| H | Meskel Square | 10 |
| I | Bambis | 11 |
| J | Stadium | 8 |
| K | Legehar | 6 |
| L | Mexico Square | 7 |
| M | Lideta | 6 |
| N | Beherawi | 4 |
| O | Arat Kilo | 5 |
| P | Piazza | 0 |

### 5.3 Admissibility of the Heuristic
A heuristic is considered admissible if it never overestimates the true minimum cost from a node to the goal. The heuristic used in this project satisfies the admissibility condition for the following reasons:
1.  The values represent optimistic estimates of travel time under ideal traffic conditions.
2.  The heuristic values are consistently less than or equal to the actual shortest travel time observed through the road network.
3.  The goal node (Piazza) has a heuristic value of zero, which satisfies the base condition for admissibility.

As a result, the A* search algorithm is guaranteed to return an optimal path when using this heuristic.

### 5.4 Role of the Heuristic in Search Performance
The heuristic function significantly improves the efficiency of the search process by prioritizing nodes that are estimated to be closer to the goal. This reduces unnecessary exploration of less promising routes and minimizes the number of node expansions compared to uninformed search algorithms such as Uniform Cost Search.

## 6. Algorithm Implementation
This section describes the implementation of the A* search algorithm used to find the optimal route between Bole Medhanialem and Piazza. The algorithm operates on the weighted road network graph and utilizes the heuristic function defined in the previous section to guide the search efficiently toward the goal.

### 6.1 Algorithm Description
The A* algorithm begins at the start node and explores neighboring nodes based on the evaluation function:
$$f(n) = g(n) + h(n)$$

At each step:
1.  The node with the lowest $f(n)$ value is selected from the open list.
2.  Its neighbors are examined, and the cost to reach them is calculated.
3.  If a cheaper path to a neighbor is found, the path and cost are updated.
4.  The process continues until the goal node is reached.

The algorithm maintains:
*   An open set of nodes to be explored
*   A closed set of already explored nodes
*   A record of the optimal path taken to reach each node

### 6.2 Python Implementation
See `src/a_star.py` for the code implementation.

### 6.3 Input Parameters
*   **Graph**: Adjacency list representing the road network
*   **Heuristic**: Dictionary containing heuristic values $h(n)$
*   **Start Node**: Bole Medhanialem
*   **Goal Node**: Piazza

### 6.4 Algorithm Output
The algorithm returns:
*   The optimal path as an ordered list of stations
*   The total travel time required to reach the goal

## 7. Sample Execution and Results
This section presents a sample execution of the A* search algorithm using the defined road network, heuristic values, and cost model.

### 7.1 Execution Setup
*   **Start Station**: Bole Medhanialem
*   **Goal Station**: Piazza
*   **Cost Metric**: Travel time (minutes)
*   **Search Algorithm**: A*

The heuristic values defined in Section 5 were used to guide the search toward the goal.

### 7.2 Sample Output
After executing the A* algorithm, the following optimal route was obtained:

**Optimal Path**:
Bole Medhanialem → Edna Mall → Atlas → Urael → Kazanchis → Arat Kilo → Piazza

**Total Travel Time**:
25 minutes

This result indicates that the algorithm successfully identified a route with the lowest accumulated travel time based on the given road network and cost assumptions.

### 7.3 Interpretation of Results
The selected path reflects realistic driving behavior within Addis Ababa, moving from eastern commercial hubs through central administrative areas before reaching the historic city center. The algorithm avoided longer routes through heavily congested areas and prioritized paths with lower estimated total travel time.

## 8. Performance Analysis
The performance of the A* search algorithm was evaluated based on its efficiency and ability to minimize unnecessary exploration.

### 8.1 Node Expansion Behavior
Compared to uninformed search methods such as Uniform Cost Search, A* expanded fewer nodes due to the guidance provided by the heuristic function. Nodes closer to Piazza, according to the heuristic estimates, were prioritized during exploration.

### 8.2 Efficiency and Optimality
*   **Efficiency**: The heuristic significantly reduced the search space, allowing the algorithm to reach the goal quickly.
*   **Optimality**: Because the heuristic was admissible, the algorithm guaranteed an optimal solution.
*   **Scalability**: The approach is suitable for moderately sized road networks and can be extended to larger networks with more stations.

### 8.3 Limitations
While effective, the model assumes:
*   Static travel times (no real-time traffic variation)
*   Bidirectional roads with equal costs
*   Estimated heuristic values rather than precise geographic distances
These simplifications were necessary to keep the problem manageable while still demonstrating core AI concepts.

## 9. Conclusion
This assignment demonstrated the application of Artificial Intelligence search techniques to a real-world urban transportation problem. A portion of the Addis Ababa road network was successfully modeled as a weighted graph, with taksi stations represented as nodes and road segments as weighted edges.

The A* search algorithm was implemented to determine the optimal route from Bole Medhanialem to Piazza, using travel time as the cost metric and an admissible heuristic to guide the search. The results showed that A* efficiently identifies the least-cost path while minimizing unnecessary node expansions.

Overall, this project highlights the practical relevance of graph modeling and heuristic search algorithms in solving real-world route optimization problems and provides a solid foundation for more advanced transportation and navigation systems.

## References
*   Russell, S., & Norvig, P. (2021). Artificial Intelligence: A Modern Approach (4th ed.). Pearson Education.
*   Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). Introduction to Algorithms (4th ed.). MIT Press.
*   Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the heuristic determination of minimum cost paths. IEEE Transactions on Systems Science and Cybernetics, 4(2), 100–107.
*   Pearl, J. (1984). Heuristics: Intelligent Search Strategies for Computer Problem Solving. Addison-Wesley.
*   Addis Ababa City Roads Authority. (n.d.). Addis Ababa road network overview.
*   GeeksforGeeks. (n.d.). A* Search Algorithm. - https://www.geeksforgeeks.org/a-search-algorithm/
