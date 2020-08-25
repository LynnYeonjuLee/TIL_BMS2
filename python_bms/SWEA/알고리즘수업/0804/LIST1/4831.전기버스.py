T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int,input().split())  # N 은 버스정류장, K 는 한 번 충전으로 최대한 이동가능 정류장 수 , M 은 충전기가 설치된 정류장 수 
    M_list = list(map(int,input().split())) # 충전기 위치 
    result = [0]*(N+1)
    
    for i in range(len(M_list)): # 정류장의 개수 리스트 인덱스를 받고 
        result[M_list][station[i]] += 1

    first = 0
    last = K
    cnt = 0
    
    while True:
        stop = 0
        for i in range(first+1, last+1):
            if result[i] == 1:
                first = i
            else:
                stop += 1
        if stop == K:
            cnt = 0
            break
        cnt += 1
        last = first + K

        if last >= N:
            break
                
    print('#{} {}.format(test_case, cnt)')