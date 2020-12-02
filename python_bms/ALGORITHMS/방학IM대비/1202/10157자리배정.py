# 자리배치도를 오른쪽으로 90도 돌려서 확인한다고 생각하자
X, Y = map(int,input().split())
N = int(input())
arr = [[0] * Y for _ in range(X)]
# print(arr)
direction = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x = 0
y = 0
newX = 0
newY = 0
num = 1

for i in range(X * Y):
    x, y = newX, newY
    if num == N:
        a = x
        b = y
    arr[x][y] = num
    newX = x + dx[direction]
    newY = y + dy[direction]

    if newX < 0 or newX >= X or newY < 0 or newY >= Y or arr[newX][newY] != 0:
        direction = (direction + 1) % 4
        newX = x + dx[direction]
        newY = y + dy[direction]

    num += 1

if N > X*Y:
    print(0)
else: # 0.0 부터 시작하니
    print(a+1, end=' ')
    print(b+1)