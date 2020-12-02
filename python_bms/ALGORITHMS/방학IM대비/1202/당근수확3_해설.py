T = int(input())
# T = 1 # 테케 하나만 보고 싶을 때
for t in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # for row in arr:
    #     print(*row)
    minV = 99999
    for i in range(1, N): # 3번 영역과 1+2번 영역의 경
        sum3 = 0
        for k in range(i, N):
            for m in range(0, M):
                sum3 += arr[k][m]
        # print("sum3:",sum3)
        # print(sum3)
        for j in range(1, M): # 1번과 2번의 경계
            sum1 = 0
            tem_max = tem_min = 0
            for k in range(0, i):
                for m in range(0, j):
                    sum1 += arr[k][m]
            tem_max = max(tem_max,sum1)
            tem_min = min(tem_max,sum1)
            # print("sum1:",sum1)
            sum2 = 0
            for k in range(0, i):
                for m in range(j, M):
                    sum2 += arr[k][m]
            tem_max = max(tem_max, sum2)
            tem_min = min(tem_max, sum2)

            minV = min(minV,abs(tem_max-tem_min))
            # print("sum2:",sum2)
    print('#{} {}'.format(t,minV))


