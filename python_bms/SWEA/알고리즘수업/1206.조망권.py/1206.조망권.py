T = 10
for tc in range(1, T+1):
    N = int(input())
    bld = list(map(int,input().split()))
    result = 0

    for i in range(2, N-2): #가로위치 별로:
        highest = max(bld[i-1], bld[i-2], bld[i+1], bld[i+2])
        if bld[i]-highest > 0:
            result += bld[i] - highest

    print('#{} {}'.format(tc,result))