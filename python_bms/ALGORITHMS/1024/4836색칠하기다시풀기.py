T = int(input())
for t in range(1, T+1):
    N = int(input())
    C1 = []
    arr = [[0]*10 for _ in range(10)]

    for n in range(N):
        # 색정보 입력받기 
        C = list(map(int,input().split()))

        for y in range(C[1],C[3]+1):
            for x in range(C[0],C[2]+1):
                arr[y][x] += C[4]
           
    cnt = 0
    for y in range(10):
        for x in range(10):
            if arr[y][x] == 3:
                cnt += 1

    print('#{} {}'.format(t,cnt))