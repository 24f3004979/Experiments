

INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)

    # Distance Matrix
    dist = [row[:] for row in graph] # why row[:]

    # CORE ALGORITgraph = [
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

# Adgecency matrix
graph = [
    [0,   3,   INF, 7],
    [8,   0,   2,   INF],
    [5,   INF, 0,   1],
    [2,   INF, INF, 0]
]

print('Floyed warshall algorithm')
print(floyd_warshall(graph))
