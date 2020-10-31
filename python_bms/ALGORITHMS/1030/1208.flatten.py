# 다른 문제랑 착각해서 어렵다고 말했나봐용!! 
for t in range(1, 11):
    dump_N = int(input())
    h = list(map(int,input().split()))
    h.sort()
    for i in range(dump_N):
        h[0] += 1
        h[-1] -= 1
        h.sort()
    print('#{} {}'.format(t,h[-1]-h[0]))

