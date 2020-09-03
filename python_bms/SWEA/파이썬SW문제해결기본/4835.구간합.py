T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int,input().split()))
    sum_list = []
    for i in range(0, N-M+1):
        sum_value = 0
        for j in range(i, i+M):
            sum_value += int(a[j])
        
        sum_list.append(sum_value)
        new_sum_list = sorted(sum_list)
        result = new_sum_list[-1] - new_sum_list[0]

    print('#{} {}'.format(tc, result))
