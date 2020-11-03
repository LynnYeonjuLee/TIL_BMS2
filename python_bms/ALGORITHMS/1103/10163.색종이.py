N = int(input())
arr = [[0]*101 for _ in range(101)]
for n in range(1, N+1):
    x, y, w, h = map(int,input().split())
    for i in range(x,x+w):
        for j in range(y,y+h):
            arr[i][j] = n
result = 0
for n in range(1, N+1):
    cnt = 0
    cnt_zero = 0
    for a in range(101):
        for b in range(101):
            if arr[a][b] == n:
                cnt += 1
            else:
                cnt_zero += 1
                if cnt_zero == 101*101:
                    cnt = 0
    print(cnt)
