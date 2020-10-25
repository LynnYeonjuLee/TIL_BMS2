T = int(input())
for t in range(1, 1+T):
    N = int(input())
    nums = list(map(int,input().split()))
    inc_nums = sorted(nums)
    dec_nums = inc_nums[::-1]
    result = []
    for i in range(5):
        result.append(dec_nums[i])
        result.append(inc_nums[i])
    print('#{} {}'.format(t,' '.join(map(str,result))))