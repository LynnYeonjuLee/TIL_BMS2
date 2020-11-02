# 아직
N = int(input())
area = 0
arr = [[0]*101 for _ in range(101)]
for _ in range(N):
    l, b = map(int,input().split())
    for j in range(b, b+10):
        for i in range(l, l+10):     
            if arr[i][j] == 0:   
                arr[i][j] = 1
for i in range(100):
    for j in range(100):
        if arr[j][i] == 1:
            area += 1
print(area)