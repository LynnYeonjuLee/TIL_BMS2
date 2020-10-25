# 1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸 
# (1, 1)에서 출발하여 (N,M)의 위치로 이동할 때 지나야 하는 최소의 칸 수 
from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, M = map(int,input().split())
maze_list = []
for _ in range(N):
    maze = list(map(int,input()))
    maze_list.append(maze)
q = deque()
check = [[False] * M for _ in range(N)]
visited = [[0]* M for _ in range(N)]
q.append((0,0))
check[0][0] = True
visited[0][0] = 1
while q: 
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if check[nx][ny] == False and maze_list[nx][ny] == 1:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                check[nx][ny] = True
print(visited[N-1][M-1])
