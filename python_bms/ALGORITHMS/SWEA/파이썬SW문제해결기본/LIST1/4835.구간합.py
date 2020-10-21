T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    numbers = list(map(int, input().split()))
    sum_list = []

    for i in range(0, N-M+1): 
        sum_value = 0
        for j in range(i, i+M):
            sum_value += int(numbers[j])
        sum_list.append(sum_value)    
        new_sum = sorted(sum_list)
        result = new_sum[-1] - new_sum[0]

    print(f'#{test_case} {result}')

