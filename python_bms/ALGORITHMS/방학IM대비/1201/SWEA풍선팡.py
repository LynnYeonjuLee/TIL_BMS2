T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    balloons = [list(map(int,input().split())) for i in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    # print(balloons)

    max_sum = 0
    sum_list = []
    for i in range(N):
        for j in range(M):
            sum_pang = 0
            sum_pang += balloons[i][j]
            for a in range(1, balloons[i][j]+1):
                for k in range(4):
                    nr = i + dr[k]*a
                    nc = j + dc[k]*a
                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        continue
                    else:
                        sum_pang += balloons[nr][nc]
                sum_list.append(sum_pang)
    # print(sum_list)
    print('#{} {}'.format(t, max(sum_list)))