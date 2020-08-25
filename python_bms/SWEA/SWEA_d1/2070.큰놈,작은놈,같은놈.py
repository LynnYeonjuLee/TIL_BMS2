T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    if numbers[0] > numbers[1]:
        print('#{} >'.format(test_case))
    elif numbers[0] == numbers[1]:
        print('#{} ='.format(test_case))
    else:
        print('#{} <'.format(test_case))