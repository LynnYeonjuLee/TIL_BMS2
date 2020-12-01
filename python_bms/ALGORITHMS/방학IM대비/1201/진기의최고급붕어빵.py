T = int(input())
for t in range(1, T+1):
    # N 사람 빵,M초의 시간 ,K개의 붕어
    N, M, K = map(int,input().split())
    secs = list(map(int,input().split())) # N 의 사람 도착 시간 정수
    result = 'Possible'

    remain = 0 # 남은 붕어빵의 수
    for i in range(11112):
        # if sorted(secs[i]) < M:
        if i != 0 and i % M == 0: # 0일 땐 안만드니까 # M의 배수일 때 붕어빵이 세 개만큼 증가
            remain += K
        for sec in secs:
            if sec == i:
                if remain == 0: # 붕어빵이 없는 경우
                    result = 'Impossible'
                    break

                remain -= 1
            # 사람이 진기가 붕어빵을 만드는 시간보다 빨리 도착할 경우 불가능
        #     result = 'Impossible'
        #     # 더이상 체크할 필요 없다.
        #     break
        # else:
            # 사람이 진기가 붕어빵을 만드는 시간보다 늦게 도착할 경우
            # 그 다음 사람의 도착 시간을 확인해야한다..
            # result = 'Possible'
            # i += 1

    print('#{} {}'.format(t,result))


