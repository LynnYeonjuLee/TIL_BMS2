T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    nums = list(map(int,input().split()))
    sum_list = []
    sum_num = 0
    for i in range(0, N-M):
        sum_num = nums[i] + nums[i+1] + nums[i-1]
        sum_list.append(sum_num)
    print('#{} {}'.format(tc, max(sum_list)))