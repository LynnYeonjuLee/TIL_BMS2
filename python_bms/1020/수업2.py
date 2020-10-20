# 스택 
# 후입선출 LIFO


# DFS
G = [[], [2, 3], [1, 4, 5,], [1, 7], [2, 6], [4, 5, 7], [3, 6]]
visited = [False] * 0

def dfsr(v):
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            dfsr(w)

def dfs(v):
    S = []
    S.append(v)
    visited[v] = True

    while S:
        v = S.pop(-1)
        for w in G[v]:
            if not visited[w]:
                S.append(w)
                visited[w] = True

# 1, 2, 1, 3, 2, 3
n = list(map(int,input().split()))
for i in range(len(n)//2):
    val1 = n[i*2]
    val2 = n[i*2+1]
    G[val1] = val2
    G[val2] = val1

