# for 문 range 쓸 때는 기준을 잡기
# -> 다른 변수를 건들지말기
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
    for j in range(sign_idx, N):
        if pw[i] == sign[j]:
            cnt = 1
            sign_idx = j + 1
            break
    if cnt == 0:
        result = 0
        break

print(result)


