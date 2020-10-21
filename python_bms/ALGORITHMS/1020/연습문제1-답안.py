dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
arr = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

def isWall(x, y):
    if x < 0 or x >= 5:
        return True
    if y < 0 or y >= 5:
        return True

val = 0
for y in range(5): 
    # 한 줄에 대해 따로따로 구하라고 했으면 val = 0  이 이 자리에 와야한다. 
    for x in range(5):
#  네 방향에 대한 새로운 위치를 정해줌 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isWall(nx, ny) != False:
                val = abs(arr[y][x] - arr[ny][nx])