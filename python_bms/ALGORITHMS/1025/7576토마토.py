from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

M, N = map(int,input().split())
t_list = []
q = deque()
for i in range(N):
    to = list(map(int,input().split()))
    for j in range(M):
        if to[j] == 1:
            q.append((i,j))
    t_list.append(to)

day = 0
while q: 
    day += 1
    for _ in range(len(q)):
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and t_list[nx][ny] == 0:
                q.append((nx,ny))
                t_list[nx][ny] = t_list[x][y] + 1
# print(t_list)      
# result = 0
# for i in range(N): 
#     for j in range(M):
#         if t_list[i][j] == 0:
#             result = -1
#         else:
#             result = day-1
# print(result)
result = []
for t in t_list:
    if 0 in t:
        result.append(-1)
if -1 in result:
    print(-1)
else: 
    print(day-1)
