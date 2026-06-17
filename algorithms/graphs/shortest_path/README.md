# Dijkstra's Shortest Path Algorithm

## Overview
Implementation of Dijkstra's algorithm using an adjacency matrix to find the shortest path between nodes in a weighted graph. This module focuses on the "relaxation" technique to iteratively optimize path distances.

## Key Learning Outcomes
- **Algorithmic Mechanics:** Implementation of the greedy strategy to update the shortest known distance to unvisited nodes.
- **State Management:** Effective use of `distances` and `paths` arrays to track cumulative weight and history.
- **Complexity Analysis:** Understanding $O(V^2)$ time complexity for matrix-based graph traversal vs. $O((V+E) \log V)$ for priority queue-based implementations.
- **Refinement:** Resolved scope-based logic errors and optimized data structure traversal, ensuring robust handling of disconnected nodes and path reconstruction.

## Usage
```python
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
]

# Get shortest path from node 0 to node 5
shortest_path(adj_matrix, 0, 5)