
import sys
sys.stdin = open("달팽이숫자_input.txt")


def solve(arr):
    x, y = 0, 0
    newX, newY = 0, 0
    dx = [0, 1,  0, -1]
    dy = [1, 0, -1,  0]
    direction =0 # 0:우, 1 :하, 2:좌 3:상
    num = 1 # 1 ~ (N*N)

    for i in range(N*N):
        x, y = newX, newY
        arr[x][y] = num
        newX = x + dx[direction]
        newY = y + dy[direction]
        if newX < 0 or newX >= N or newY < 0 or newY >= N or arr[newX][newY] != 0:
            direction = (direction + 1) % 4
            newX = x + dx[direction]
            newY = y + dy[direction]

        num += 1

T = int(input())
for tc in range(T):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    # print(arr)

    solve(arr)
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=" ")
        print()