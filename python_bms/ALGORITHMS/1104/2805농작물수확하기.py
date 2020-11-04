# 왜때문에 몇번을 풀어도...헷갈리는가ㅜㄹ,ㅠ,트
T = int(input())
for t in range(1, T+1):
    N = int(input())
    farm = []
    for _ in range(N):
        nums = list(map(int,input()))
        farm.append(nums)
    result = 0
    mid = N//2
    step = 0
    for i in range(N):
        for j in range(N):
            # if i < N//2:
            # elif i == N//2:
            #     result += farm[i][j]
            # else: 
            for n in range(mid+step, mid+step+1):
                result +=  
