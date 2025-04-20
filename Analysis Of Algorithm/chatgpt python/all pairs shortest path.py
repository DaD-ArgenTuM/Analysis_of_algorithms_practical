# Function to implement Floyd-Warshall algorithm
def floyd_warshall(graph):
    n = len(graph)
    
    # Initialize distance matrix (copy of graph)
    dist = [row[:] for row in graph]

    # Apply Floyd-Warshall DP
    for k in range(n):  # intermediate vertex
        for i in range(n):  # source
            for j in range(n):  # destination
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage:
INF = float('inf')
graph = [
    [0,     3,    INF,   5],
    [2,     0,    INF,   4],
    [INF,   1,    0,     INF],
    [INF,   INF,  2,     0]
]

result = floyd_warshall(graph)

# Print the result
print("All-Pairs Shortest Paths:")
for row in result:
    print(row)
