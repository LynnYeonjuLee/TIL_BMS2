from pprint import pprint

paint = [[0]*200 for _ in range(200)]
N, M = map(int,input().split())
cnt = 0
for _ in range(N):
    x1, y1, x2, y2 = list(map(int,input().split()))
    for r in range(y1, y2+1):
        for c in range(x1, x2+1):
            paint[r][c] += 1
# pprint(paint)
for r in range(200):
    for c in range(200):
        if paint[r][c] > M:
            cnt += 1
print(cnt)
# print(paint)

'''
3 1
1 1 1 1
1 1 1 1
1 1 1 1
'''