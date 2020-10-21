T = int(input())
for tc in range(1, T+1):
    nums = list(map(int,input().split()))
    largest = 0 
    for num in nums:
        if num > largest:
            largest = num
    print('#{} {}'.format(tc, largest))