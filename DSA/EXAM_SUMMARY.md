A concise summary of all Data Structures and Algorithms implemented in this repo.

## 1. Shortest Path Algorithms (SSSP & APSP)
*   **Dijkstra’s (`dijkstras.py`)**: 
    *   **Goal:** Single Source Shortest Path (SSSP).
    *   **Constraint:** Only for **non-negative** weights.
    *   **Logic:** Greedy approach; uses a "visited" set and relaxes edges iteratively.
*   **Bellman-Ford (`bellmanford.py`)**:
    *   **Goal:** SSSP for graphs with **negative weights**.
    *   **Feature:** Can detect **negative weight cycles** (if distance keeps decreasing after $V-1$ iterations).
*   **Floyd-Warshall (`floyed_warshall.py`)**:
    *   **Goal:** All-Pairs Shortest Path (APSP).
    *   **Logic:** Dynamic Programming ($O(V^3)$). Uses an intermediate vertex $k$ to check if $i \to k \to j$ is shorter than $i \to j$.

## 2. Minimum Spanning Trees (MST)
*   **Prim’s (`prims.py`)**:
    *   **Logic:** Start from a node, greedily pick the cheapest edge connecting to an unvisited node using a **Min-Heap**.
    *   **Application:** Useful for "dense" graphs or route planning (`routes_planning.txt`).
*   **Kruskal’s (`making_spanning.py`)**:
    *   **Logic:** Sort all edges by weight, add them if they don't form a cycle (using Disjoint Set Union).

## 3. Directed Acyclic Graphs (DAG)
*   **Topological Sort (`topological_sorting.py`)**:
    *   **Goal:** Linear ordering of vertices such that for every edge $u \to v$, $u$ comes before $v$.
    *   **Algorithm:** Kahn’s Algorithm (using **In-degrees**) or DFS.
*   **Dependency Resolution (`dependency.py`)**: 
    *   Practical application of Topological Sort (e.g., semester course planning).

## 4. Search & Optimization
*   **Binary Search in Rotated Arrays (`rotating.py`, `find_min.py`)**:
    *   Finding the minimum in a sorted but rotated list (e.g., `[3,4,5,1,2]`) in $O(\log n)$.
*   **Heaps & Kth Minimum (`problems-dive/learning.md`)**:
    *   Using **Min-Heaps** for efficient retrieval.
    *   **Pro Tip:** Use a Max-Heap (negative signs) of size $K$ to find the Kth smallest element in one pass.

## 5. Key Problem Scenarios
*   **Route Planning:** Use Prim's or Dijkstra's.
*   **Cycle Detection:** Topological sort (if not all nodes visited) or Bellman-Ford (for negative cycles).
*   **Path Reconstruction:** Storing the "predecessor" during relaxation.
