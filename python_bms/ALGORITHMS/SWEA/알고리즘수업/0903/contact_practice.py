import sys
sys.stdin = open("input.txt")

def bfs(v):
    q = []
    q.append(v)
    visited[v] = 1

    while q:
        v = q.pop(0)
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] +1 
                                                                               
for tc in range(1, 11): # 테스트케이스는 10개이므로 따로 T를 받지 않는다. 
    # 정점의 수 - N , 시작 값 - v
    N, v = map(int, input().split())
    # 
    temp = list(map(int, input().split()))
    G = [[] for _ in range(101)]
    for i in range(len(temp)//2):
        s, e = temp[2*i], temp[2*i+1]
        G[s].append(e)

    visited = [0] * 101
    bfs(v)
    visited_max = max(visited)
    visited.reverse()

    print('#{}'.format(tc), end= ' ')
    print(len(visited)-visited.index(visited_max)-1)
