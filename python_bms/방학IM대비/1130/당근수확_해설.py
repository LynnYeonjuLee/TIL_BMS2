T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    # print(arr)
    minV = 999
    minidx = 0 # 첫 일꾼의 마지막 영역을 저장하자
    for i in range(1, N):
        sum1 = sum2 = 0
        for j in range(0, i):
            sum1 += arr[j]
        for j in range(i+1, N):
            sum2 += arr[j]
        # print(sum1, sum2)
        diff = abs(sum1-sum2)
        if minV > diff:
            minV = diff
            minidx = i
    print('#{} {}'.format(t, minidx, minV))