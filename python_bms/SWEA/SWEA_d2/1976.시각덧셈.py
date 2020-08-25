T = int(input())
for test_case in range(1, T+1):
    nums = list(map(int,input().split()))
    mins = 0
    hrs = 0
    for num in range(4):
        mins = nums[1] + nums[3]
        if mins > 59:
            mins -= 60
            hrs = nums[0] + nums[2] + 1
            if hrs > 12:
                hrs -= 12
        else:  
            hrs = nums[0] + nums[2]
            if hrs > 12:
                hrs -= 12
    print(f'#{test_case} {hrs} {mins}')
