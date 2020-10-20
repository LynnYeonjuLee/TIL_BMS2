def isSafe(y,x):
    return 0<=y<N and 0<=x<N and (maze[y][x] == 0 or maze[y][x] == 3)

def dfsr(sy, sx):
    global result

    if maze[sy][sx] == 3:
        result = 1
        return

    visited.append((sy, sx))
    for i in range(4):
        ny = sy + dy[i]
        nx = sx + dx[i]
        if isSafe(ny, nx) and (ny, nx) not in visited:
            cnt += 1
            dfsr(ny, nx)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                sy, sx = y,x

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = []
    result = 0
    dfsr(sy, sx)
    print('#{} {}'.format(t, result))