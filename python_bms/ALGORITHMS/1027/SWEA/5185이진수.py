T = int(input())
for t in range(1, T+1):
    N, S = input().split()
    a = int(S,16) # 16진수를 10진수로 
    a = format(a,'b') # 2진수로 
    if len(a) < int(N) * 4:
        a = '0' + a
    print('#{} {}'.format(t, a))