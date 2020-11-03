T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    flies = []
    for n in range(N):
        fly = list(map(int,input().split()))
        flies.append(fly)
    sum_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for a in range(i,i+M):
                for b in range(j,j+M):
                    cnt += flies[a][b]
                sum_list.append(cnt)
    print('#{} {}'.format(t, max(sum_list)))