# result= 1 아니면 0출력
K, N = list(map(int,input().split()))
# N : 신호의 길이
# K : 암호의 길이
pw = list(map(int,input()))
sign = list(map(int,input()))
pw_idx = 0
sign_idx = 0
result = 1
for i in range(K):
    cnt = 0
    for j in range(sign_idx,N):
        if pw[i] == sign[j]:
            cnt = 1
            sign_idx = j + 1
            break
        # else:
        #     continue
    if cnt == 0:
        result = 0
        break
print(result)
NONONOONNON
