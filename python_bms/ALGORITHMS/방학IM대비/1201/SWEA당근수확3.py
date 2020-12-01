T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    carrots = []
    for _ in range(N):
        carrots.append(list(map(int,input().split())))
    # print(carrots)
    # 1, 2, 3 번 일꾼 중 3번 일꾼의 합을 먼저 구한다.

    sum3_list = []
    start = 1
    for i in range(start, N): # 적어도 첫째줄은 1번과 2번이 나누어 가져갈테니
        sum3 = 0
        for j in range(M):
            sum3 += carrots[i][j]

            start += 1
        # print(sum3)
        sum3_list.append(sum3)

    # print(sum3_list) # 16, 17, 12
    sum3_list_real = []
    sum3_list_real.append(sum3_list[-1])
    for i in range(1, len(sum3_list)):
        sum3_list_real.append(sum3_list_real[-1]+sum3_list[-(i+1)])
    # print(sum3_list_real) # 12, 29, 45  (순서 반대로)
    sum1_list = []
    end = 0
    sum1 = 0

    for j in range(M):
        start = 1
        # for k in range(N-2):
        for i in range(N-start):
            if start <= N:
                sum1 += carrots[i][j]
        sum1_list.append(sum1)
        start += 1
        print(sum1)
    print(sum1_list) # 15, 26, 39, 57
    # sum2 = sum(carrots)-sum1_list[]-sum3_list_real[]

