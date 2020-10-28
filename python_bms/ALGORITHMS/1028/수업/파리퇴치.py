T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    max_cnt = 0
    flies_list = []
    for _ in range(N):
        flies = list(map(int,input().split()))
        flies_list.append(flies)
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt = 0
            for a in range(i, i+M):
                for b in range(j, j+M):
                    cnt += flies_list[a][b]
            if cnt > max_cnt:
                max_cnt = cnt
    print('#{} {}'.format(t, max_cnt))
