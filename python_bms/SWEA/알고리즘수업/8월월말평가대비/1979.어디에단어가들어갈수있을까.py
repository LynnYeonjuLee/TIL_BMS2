T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    puzzle = [list(map(int,input().split())) for _ in range(N)]
    answer = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 0:
                if cnt == K:
                    answer += 1
                cnt = 0
                continue
            cnt += 1
        if cnt == K:
            answer += 1
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 0:
                if cnt == K:
                    answer += 1
                cnt = 0
                continue
            cnt += 1
        if cnt == K:
            answer += 1
    print('#{} {}'.format(tc, answer))