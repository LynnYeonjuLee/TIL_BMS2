N = int(input())
temp = [[0]*500 for _ in range(500)]
cnt = 0
for _ in range(N):
    x1, y1, x2, y2 = list(map(int,input().split()))
    for r in range(y1, y2):
        for c in range(x1, x2):
            if temp[r][c] == 0:
                temp[r][c] = 1
                cnt += 1
print(cnt)
