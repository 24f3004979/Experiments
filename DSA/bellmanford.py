def bellmanford_list(WList, s):
    infinity = float('inf')
    distance = {}
    for v in WList.keys():
        distance[v] = infinity

    distance[s]=0
    print(f"Distance Listing : {distance}")

    # Shortest Distance from source
    for _ in WList.keys():
        for u in WList.keys(): # Refrence root for neighbour
            for v,d in WList[u]: # neighbour refrence distance
                if distance[v] > distance[u] + d:
                    distance[v] = distance[u] + d
    return distance

