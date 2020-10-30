dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
import sys
sys.setrecursionlimit(10**6) #재귀 깊이 설정 (10만 -> 100만)

def dfs(x, y, _cnt):
    dist[x][y] = _cnt

    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if a[nx][ny] == 1 and dist[nx][ny] == -1:
                dfs(nx, ny, _cnt)



t = int(input())
for _ in range(t):
    m, n, c = map(int, input().split())
    a = [[0] * m for _ in range(n)]
    dist = [[-1]*m for _ in range(n)]
    cnt = 0

    for _ in range(c):
        i, j = map(int, input().split())
        a[j][i] = 1

    # dfs 탐색
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and dist[i][j] == -1:
                cnt += 1
                dfs(i, j, cnt)

    print(cnt)
    
    
각 단지별 집의 개수를 구하고 싶으면,
from collections import Counter
from functools import reduce

ans = reduce(lambda x,y : x+y, dist)
ans = [x for x in ans if x>0]
ans = Counter(ans).values()



# from collections import deque

# dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# def bfs(x, y, _cnt):
#     # 시작점
#     q = deque()
#     q.append((x, y))
#     dist[x][y] = _cnt

#     while q:
#         x, y = q.popleft()

#         for k in range(4):
#             nx, ny = x+dx[k], y+dy[k]

#             if 0<=nx<n and 0<=ny<m:
#                 if a[nx][ny] == 1 and dist[nx][ny] == -1:
#                     q.append((nx, ny))
#                     dist[nx][ny] = _cnt


# t = int(input())
# for _ in range(t):
#     cnt = 0
#     n, m, c = map(int, input().split())
#     a = [[0] * m for _ in range(n)]
#     dist = [[-1]*m for _ in range(n)]

#     for _ in range(c):
#         i, j = map(int, input().split())
#         a[i][j] = 1

#     # bfs 탐색
#     for i in range(n):
#         for j in range(m):
#             if a[i][j] == 1 and dist[i][j] == -1:
#                 cnt += 1
#                 bfs(i, j, cnt)

#     print(cnt)