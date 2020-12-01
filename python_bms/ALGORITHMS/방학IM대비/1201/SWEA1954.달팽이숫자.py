T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr =[[0] * N for _ in range(N)]
    direction = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = 0
    y = 0
    newX = 0
    newY = 0
    num = 1
    for i in range(N*N):
        x, y = newX, newY
        arr[x][y] = num
        newX = x + dx[direction]
        newY = y + dy[direction]
        if newX < 0 or newX >= N or newY < 0 or newY >= N or arr[newX][newY] !=0:
            direction = (direction + 1) % 4
            newX = x + dx[direction]
            newY = y + dy[direction]
        num += 1
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()