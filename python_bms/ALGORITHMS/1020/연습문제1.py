arr = [[0] * 5 for i in range(5)]
# print(arr)
dx = [0, 0, -1, 1] # 상하좌우
dy = [-1, 1, 0, 0]
abs_= 0
cnt_abs = 0
result = 0
for x in range(5):
    for y in range(5):
        for k in range(4):
            nx = x + dx[k] 
            ny = y + dy[k]
            if ny < 0 or nx < 0 or ny >= y or nx >= x:
                continue
            else:
                abs_ = abs(arr[nx][ny] - arr[x][y])
                cnt_abs += abs_
        result += cnt_abs
print(result)
