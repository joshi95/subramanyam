# n = 5
# graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# def addEdge(u, v, weight, directed):
#     graph[u][v] = weight
#     if not directed:
#         graph[v][u] = weight

# if __name__ == "__main__":
#     addEdge(1, 2, 1, False)
#     addEdge(0, 3, 10, False)
#     addEdge(2, 3, 8, False)
#     addEdge(3, 2, 11, False)
#     addEdge(2, 5, 133, False)

#     for i in range(n + 1):
#         for j in range(n + 1):
#             print(graph[i][j], end=" ")
#         print()
       


# adjaceny list
graph = dict()

def addEdge(u, v, weight, directed):
    if u not in graph:
        graph[u] = list()
    
    graph[u].append((v, weight))

    if not directed:
        if v not in graph:
            graph[v] = list()
        graph[v].append((u, weight))


if __name__ == "__main__":
    addEdge(1, 2, 1, False)
    addEdge(0, 3, 10, False)
    addEdge(2, 3, 8, False)
    addEdge(3, 2, 11, False)
    addEdge(2, 5, 133, False)

    for key, value in graph.items():
        print(f"{key} has neighbors {value}")