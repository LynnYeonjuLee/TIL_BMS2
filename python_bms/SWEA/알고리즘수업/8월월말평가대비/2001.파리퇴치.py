T= int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    flies = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for a in range(i, i+m):
                for b in range(j, j+m):
                    temp += arr[a][b]
            if temp > flies:
                flies = temp

    print(f'#{test_case} {flies}')