
graph = dict()


def bfs(src):
    visited = [False] * 10005
    queue = []

    queue.append(src)
    visited[src] = True

    while len(queue) != 0:
        x = queue.pop(0)
        print(x)
        for neibour, _ in graph[x]:
            if not visited[neibour]:
                queue.append(neibour)
                visited[neibour] = True

def dfs(src, visited):
    print(src)
    visited[src] = True

    for neibour, wt in graph[src]:
        if not visited[neibour]:
            dfs(neibour, visited)



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

    bfs(0)
    print("dfs traversal")
    visited = [False] * 10005
    dfs(0, visited)
