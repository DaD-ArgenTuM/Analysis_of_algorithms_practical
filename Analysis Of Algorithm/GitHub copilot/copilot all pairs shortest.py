# Floyd-Warshall Algorithm for All-Pairs Shortest Path

def floyd_warshall(graph):
    # Number of vertices in the graph
    V = len(graph)

    # Initialize the distance matrix with the input graph
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    # Dynamic programming: Update distances
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # Update the distance if a shorter path is found
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage
if __name__ == "__main__":
    # Input graph represented as an adjacency matrix
    INF = float('inf')  # Use INF to represent no direct path
    graph = [
        [0, 3, INF, 5],
        [2, 0, INF, 4],
        [INF, 1, 0, INF],
        [INF, INF, 2, 0]
    ]

    # Compute all-pairs shortest paths
    shortest_paths = floyd_warshall(graph)

    # Print the result
    print("All-Pairs Shortest Paths:")
    for row in shortest_paths:
        print(row)