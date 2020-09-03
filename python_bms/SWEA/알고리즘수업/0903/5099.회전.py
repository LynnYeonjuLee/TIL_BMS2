T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    lst = list(map(int,input().split()))
    
    for i in range(M):
        t = lst.pop(0)
        lst.append(t)
    print('#{} {}'.format(tc, lst[0]))