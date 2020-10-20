def isSafe(y,x):
    return 0 <= y < N and 0<= x < N and (maze[y][x] == 0 or maze[y][x] == 3)

def bfs(sy, sx):
    global result
    q.append((sy, sx))
    visited.append((sy, sx))

    while q:
        sy, sx = q.pop(0)
        for i in range(4):
            ny = sy + dy[i]
            nx = sx + dx[i]
            if isSafe(ny, nx) and (ny, nx) not in visited:
                q.append((ny, nx))
                visited.append((ny, nx))
                distance[ny][nx] = distance[sy][sx] +1
                if maze[ny][nx] == 3:
                    result = distance[ny][nx]-1
                    return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                sy, sx = y, x

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    result = 0
    q = []
    distance = [[0]*N for _ in range(N)]
    bfs(sy, sx)
    print('#{} {}'.formant(t, result))