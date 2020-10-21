T = int(input())
for tc in range(1, T+1):
    nums = list(map(int,input().split()))
    result = 0
    for num in nums:
        if num % 2:
            result += num
    print('#{} {}'.format(tc,result))