def dfs(node):
    visited[node] = False
    for i in graph[node]:
        if visited[i]:
            dfs(i)
 
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [True for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    start, end = map(int, input().split())
    dfs(start)
    result = 1
    if visited[end]:
        result = 0
    print("#{} {}".format(tc, result))