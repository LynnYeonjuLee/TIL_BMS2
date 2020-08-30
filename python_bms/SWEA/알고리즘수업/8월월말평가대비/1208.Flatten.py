for tc in range(1, 11):
    N = int(input())
    nums = list(map(int,input().split()))
    # 가장 큰 값과 작은 값을 구하고 
    nums.sort()
    for _ in range(N):
       
        nums[0] += 1
        nums[-1] -= 1
        nums.sort()
    print('#{} {}'.format(tc, nums[-1]-nums[0]))
    # 큰값에서 -1을 , 작은값에 +1을 해준다. 
