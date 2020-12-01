T = int(input())
for t in range(1, T+1):
    N, M = list(map(int,input().split())) # N 은 필요 없음 M은 수레 용량
    carrots = list(map(int,input().split()))
    carrage = 0
    cnt = 0
    i = 0
    # N_list = []
    # for i in range(N):
    #     N_list.append(i)
    while i < N:
        if carrots[i] <= M:
            carrage += carrots[i]
            cnt += 2*i * ((carrage+carrots[i]) // M)
            # cnt += 2*i
            i += 1
        else: # M 보다 큰 경우
            if (carrage + carrots[i]) % M == 0: #M 의 배수라면 carrage 변화 없이 넘어간다.
                cnt += 2*i * ((carrage + carrots[i]) // M)
            else: # 배수가 아니라 나머지가 남는다면

                cnt += 2 * i * ((carrage + carrots[i]) // M) # 일단 나머지 이전의 배수들 만큼 왕복 해주고
                carrage += (carrage + carrots[i]) % M
                # cnt += 2 * i * ((carrage + carrots[i]) // M)
            i += 1
        if carrage > 0:
            cnt += (2*N)

    print(cnt)

        # cnt += 2*i * ((carrage+carrots[i]) // M) # 이만큼 인덱스 횟수+1 을 더하기
        #
        #      # 지금은 0으로 돌아온 상태
        #     i += 1
        # else:
        # # 수레 용량을 채우지 못하고 남은 것들은
        # # 그 다음 칸의 당근들과 합한다.
        #     cnt += 2 * i * ((carrage + carrots[i]) // M) # 일단 M 이 채워지는 만 옮겨주고
        #     carrage = carrots[i] % M
        #
        #     # cnt += 2* i * ((carrage + carrots[i+1]) // M) # 지금은 0으로 돌아온 상태
        #     i += 1



    print(cnt)





