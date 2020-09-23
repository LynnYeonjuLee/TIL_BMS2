import sys
sys.stdin = open("파리퇴치_input")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]* N for _ in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    # print(arr)

    max_answer = 0
    for x in range(N):
        for y in range(N):
            temp = 0
            for k in range(M):
                for q in range(M):
                    if 0 <= x+k < N and 0 <= y+q < N:
                        temp += arr[x+k][y+q]
            if max_answer < temp:
                max_answer = temp
    print('#{} {}'.format(tc, max_answer))