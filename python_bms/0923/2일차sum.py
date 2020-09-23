import sys
sys.stdin = open("2일차sum_input.txt")
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    maxV = 0
    # 행우선
    for i in range(100):
        sumV = 0
        for j in range(100):
            sumV += arr[i][j]
        if maxV < sumV:
            maxV = sumV

    # 열방향
    for j in range(100):
        sumV = 0
        for i in range(100):
            sumV += arr[i][j]
        if maxV < sumV:
            maxV = sumV

    #대각선1
    sumV = 0
    for i in range(100):
        sumV += arr[i][i]
    if maxV < sumV:
        maxV = sumV

    # 대각선2
    sumV = 0
    for i in range(100):
        sumV += arr[i][99-i]
    if maxV < sumV:
        maxV = sumV


    print('#{} {}'.format(tc, maxV))