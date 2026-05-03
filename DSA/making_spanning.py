'''
Problem : To Find the minimum cost for the given graph with excluding one node

Initial Wrong procedure
    Removing node from the list straight

Improvement
    Removing a Node means to remove it form the given graph
    Removing its dependency from hte graph

Iterating other parts with min_heap listing for spanning whole graph
    Logic core
    if not visited
    add to path
        iterate neighbours
        add them into heap

    How minimum cost path is discoverd
        Simply having priority with the heapq
        we wont visit big costs node unless all cheap options are visited
        resulting in automatic solving of such problem
'''
import heapq

def connectCamp(Alist, exCamp):
    # Filteration Iteration loop
    filtered_graph = {}
    for e in Alist.keys():
        if e == exCamp:
            continue # exclude the whole vertex connections
        for _ in Alist[e]:
            v, w = _
            if v == exCamp:
                continue # exclude the connection
            filtered_list[e].append((v,w)) # Filtered elements without exCamp

        # Iteration for Path finding
        visited = set()
        total_cost = 0
        start_node = list(filtered_graph.keys())[0]
        min_heap = [(0,start_node)] # weight, node <-- For running queue with weights
        path = []  # final validation logic about valid path optained or not

        # Exhausting the given min_heap
        while min_heap:
            element = heapq.heappop(min_heap)
            node, weight = element
            if node in visited:
                continue # excluding visited for loop prevention
            total_cost += weight
            visited.add(node)
            path.append(node)

            # iter neighbours for othre candidate
            for neigh in filtered_graph[node]:
                heapq.heappush(min_heap, (w,v))
        if len(path) != len(filtered_graph):
            return -1 # not a valid path found
        return total_cost

# TODO : Make Notes about all questions solved till now and be prepared with their execution study
