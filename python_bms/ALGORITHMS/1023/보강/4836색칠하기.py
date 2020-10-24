def check(x1,y1,x2,y2,color,arr):

    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            arr[y][x] += color # 이렇게 쓰면 짧다! 
            # if color == 1:
            #     arr[y][x] += 1
            # if color == 2:
            #     arr[y][x] += 2 

T = int(input())
for t in range(1, T+1):
    N = int(input())
    C1 = []
    for n in range(N):
        # 색정보 입력받기 
        C = list(map(int,input().split()))
        C1.append(C)
    # 빈 10*10 배열
    arr = [[0]*10 for _ in range(10)]

    for c in C1:
        check(c[0],c[1],c[2],c[3],c[4],arr)

    cnt = 0
    for y in range(10):
        for x in range(10):
            if arr[y][x] == 3:
                cnt += 1

    print('#{} {}'.format(t,cnt))