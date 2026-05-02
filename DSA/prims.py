'''
Making Prims algorithm
    Working flow 

    make the minimum spanning route for the whole graph without cycles

    Initializaiton requirements
        visited status, spanning path

Main Root logic
    Iterate node -> Explore its neighbour who have least track for next traversal

'''
import heapq

def prims(graph , start):
    visited = set()
    min_heap = [(0, start)] # weight, Node <-- Refrence due to min heap inits with weights
    total_cost = 0
    span = []

    while min_heap:
        element = heapq.heappop(min_heap)
        if element in visited:
            continue # Keep iteration with the given procedure

        visited.add(element)
        span.append(element)  # ELement appended into the span 
        for w,v in graph[element]:
            if not(v in visited):
                heapq.heappush((w,v), min_heap) # New elements for iteration
    return span

