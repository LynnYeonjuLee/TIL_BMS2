T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    carrots = []
    for _ in range(N):
        carrots.append(list(map(int,input().split())))
    # print(carrots)
    # 1, 2, 3 번 일꾼 중 3번 일꾼의 합을 먼저 구한다.

    sum3_list = []
    for a in range(N):

        # for b in range(M):
        for i in range(a, N):
            sum3 = 0
            for j in range(M):
                sum3 += carrots[i][j]
            sum3_list.append(sum3)
    print(sum3_list)
    sum12_list = []

    for j in range(M):
        for a in range(N):
            sum12 = 0
            for i in range(0,a+1):
                sum12 += carrots[i][j]
        sum12_list.append(sum12)
    print(sum12_list)
