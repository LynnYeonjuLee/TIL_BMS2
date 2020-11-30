T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int,input().split()))
    remain = 0
    dist = 0
    for i in range(N):
        time = (remain + arr[i]) // M # 왕복 횟수
        remain = (remain + arr[i]) % M # 남은 당근 수
        dist += ((i+1) * 2 * time)
    if remain > 0:
        dist += (2*N) # 마지막 칸에 남은 당근 횟수
    print('#{} {}'.format(t, dist))

