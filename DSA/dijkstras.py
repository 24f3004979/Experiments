def dijkstras_list(WList, s):
    '''
    Algorithm for searching for the shortest distance for given source to other nodes in the graph
        Iterating the all neighbours of the given node and switching their visited status
        iterating those nodes for their parteners and updating the distance, ultimately leading for minimizing the total distance from the source
    '''
    infinity = float('inf')
    (visited, distance) = {},{} # visited status, distance computed

    for v in WList.keys():
        visited[v], distance[v] = False, infinity
    
    distance[s] = 0  # starting vertex

    # compute shortest distance for each vertex-outer loop
    for u in WList.keys():
        min_dist = min([distance[v] for v in WList.keys() if not visited[v]])

        next_list = [v for v in WList.keys() if (not visited[v]) and (distance[v] == min_dist)] # Listing all elements with minimum distance

        # Selecting element from numerical context
        next_visiting = min(next_list)
        visited[next_visiting] = True

        # Iterating over adjacent vertex 
        for (v,d)  in WList[next_visiting]:
            if distance[v] > distance[next_visiting] + d:  # Its like feteching information from other nodes references
                distance[v] = distance[next_visiting] + d

    return distance
    
