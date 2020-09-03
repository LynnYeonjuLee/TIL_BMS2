def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

while q:
    v = q.pop(0)
    for w in G[v]:
        if not visited[w]:
            q.append(w)
            visited[w] = visited[v] + 1
for tc in range(1, 11):

N, v = map(int, input().split())
temp = list(map(int, input().split()))
G = [[] for _ in range(101)]
for i in range(len(temp)//2):
    s, e = temp[2 * i], temp[2 * i + 1]
    G[s].append(e)
visited = [0] * 101
bfs(v)
visit_max = max(visited)
visited.reverse()

print("#{}".format(tc), end=' ')
print(len(visited)-visited.index(visit_max)-1)