# 암호 : pw , 신호 : sign
# result= 1 아니면 0출력
K, N = list(map(int,input().split()))
# N : 신호의 길이
# K : 암호의 길이
pw = list(map(int,input()))
sign = list(map(int,input()))
pw_idx = 0
sign_idx = 0
cnt = 0
while sign_idx < N:
    if pw[pw_idx] == sign[sign_idx]:
        pw_idx += 1
        sign_idx += 1
        cnt += 1
    else:
        sign_idx += 1
if cnt == K:
    result = 1
else:
    result = 0
print(result)
print(sign)
nononnononno