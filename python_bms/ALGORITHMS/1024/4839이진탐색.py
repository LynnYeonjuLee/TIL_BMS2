T = int(input())
for t in range(1, T+1):
    P, A, B = list(map(int,input().split()))
    cnt_A = 0
    cnt_B = 0
    l1 = 1
    r1 = P
    l2 = 1
    r2 = P
    c1 = 0
    c2 = 0
    result = ''
    while A != c1:
        c1 = int((l1+r1)/2)
        cnt_A += 1
        if A > c1:
            l1 = c1
        elif A == c1:
            break
        else:
            r1 = c1
    while B != c2:
        c2 = int((l2+r2)/2)
        cnt_B += 1
        if B > c2:
            l2 = c2
        elif B == c2:
            break
        else:
            r2 = c2
    if cnt_A > cnt_B:
        result = 'B'
    elif cnt_A == cnt_B:
        result = 0
    else:
        result = 'A'

    print('#{} {}'.format(t, result))

 
