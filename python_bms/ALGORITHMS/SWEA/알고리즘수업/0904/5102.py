def bfs(q):
    cnt = 1
    while q:
        s_q = []
        while q:
            idx = q.pop()
            for i in node[idx]:
                if visited[i]: continue
                if i == end: return cnt
                s_q.append(i)
                visited[i] = 1
        cnt += 1
        q = s_q
    return 0
 
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    start, end = map(int, input().split())
    visited[start] = 1
    print('#{} {}'.format(tc, bfs([start])))