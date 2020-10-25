# 요거 어렵어렵..
# 비트와 조합으로 각각 풀어볼랭 

T = int(input())
for t in range(1, T+1):
    N, K = map(int,input().split())
    cnt = 0
    for n in range(1<<12): # 갯수만큼 돌려줌
        sum = 0
        count = 0 # 갯수
        for bit in range(12):
            if (n & (1<<bit)) > 0:
                sum += (bit+1)
                count += 1
        # 6 -> 5 
        if K == sum and count == N:
            cnt += 1
    print('#{} {}'.format(t, cnt))

    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

        


