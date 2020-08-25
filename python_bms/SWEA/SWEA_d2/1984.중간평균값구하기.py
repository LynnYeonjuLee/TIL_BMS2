T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int,input().split()))
    new_numbers = sorted(numbers)
    sum = 0

    for i in range(1, 9):
        sum += new_numbers[i]
    
    result = sum / 8
    print(f'#{test_case} {round(result)}')