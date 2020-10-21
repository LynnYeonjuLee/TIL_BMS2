T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    result = max(a)
    print(f'#{test_case} {result}')