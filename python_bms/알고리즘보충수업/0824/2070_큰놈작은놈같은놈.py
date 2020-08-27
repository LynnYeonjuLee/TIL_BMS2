T = int(input())
for tc in range(1, T+1):
    nums = list(map(int,input().split()))
    if nums[0] > nums[1]:
        result = '>'
    elif nums[0] == nums[1]:
        result = '='
    else: 
        result = '<'
    print('#{} {}'.format(tc, result))
    

