T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    max_num = nums[0]
    min_num = nums[0]
    for num in nums:
        if max_num < num:
            max_num = num
        if min_num > num:
            min_num = num
    result = max_num - min_num
    print('#{} {}'.format(t,result))