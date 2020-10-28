temp = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for r in range(y1, y2):
        for c in range(x1, x2):
            if temp[r][c] == 0:
                temp[r][c] = 1
                cnt += 1
print(cnt)

