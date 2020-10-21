T = int(input())
for tc in range(1, T+1):
    nums = list(map(int,input().split()))
    sum_num = 0
    len_num =len(nums)
    for num in nums:
        sum_num += num
    result = sum_num / len_num
    print('#{} {}'.format(tc, round(result)))