T = 10
for tc in range(1, T+1):
    N = int(input())
    floors = list(map(int,input().split()))
    result = 0

    for i in range(2, N-2):
        highest = max(floors[i-2],floors[i-1],floors[i+1],floors[i+2])
        if floors[i] > highest:
            result += floors[i]-highest
    print('#{} {}'.format(tc, result))

