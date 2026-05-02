from dijkstras import *
from prims import *
from bellmanford import *

# making simple graph for testing
listing = [
    ('A', 'B', 4),
    ('A', 'C', 2),
    ('B', 'C', 5),
    ('B', 'D', 10),
    ('C', 'D', 3),
    ('D', 'E', 1),
    ('C', 'E', 8)
]# Simple weighted adjacency listing
graph = {}
for i in listing:
    s,v,w = i
    graph[s] = []
    graph[v] = []

print(f"Graph Initiated : {graph}")

for _ in listing:
    e = (_[1], _[2])
    graph[_[0]].append(e)

# Testing prims algorithm 
print(prims(graph, 'A'))
