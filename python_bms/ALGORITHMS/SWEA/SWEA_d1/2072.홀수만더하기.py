T = int(input())
for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    total = 0
    for number in numbers:
        if number % 2:
            total += number
        else:
            total = total
    print('#{} {}'.format(test_case, total))