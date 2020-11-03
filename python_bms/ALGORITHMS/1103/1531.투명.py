paint = [[0]*100 for _ in range(100)]
N, M = map(int,input().split())
cnt = 0
for _ in range(N):
    x1, y1, x2, y2 = list(map(int,input().split()))
    for r in range(y1, y2+1):
        for c in range(x1, x2+1):
            paint[c][r] += 1
    
    for r in range(y1, y2+1):
        for c in range(x1, x2+1):
            if paint[c][r] > M:
                cnt += 1
print(cnt)