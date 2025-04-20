def floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

# Example
INF = float('inf')
graph = [
    [0,   1,   4,   INF],
    [INF, 0,   2,   6],
    [INF, INF, 0,   3],
    [7,   INF, INF, 0]
]


result = floyd_warshall(graph)

# Print result
for row in result:
    print(row)
