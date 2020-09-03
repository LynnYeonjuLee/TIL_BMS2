T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    for i in range(E):
        sp, ep = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for i in range(V+1):
        G[sp].append(ep)
    s, e = map(int, input().split())
    print(G)
