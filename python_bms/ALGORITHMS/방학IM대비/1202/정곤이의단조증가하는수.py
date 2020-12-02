T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    num_list = []
    for i in range(N):
        for j in range(i+1, N):
            num_list.append(nums[i] * nums[j])
    if len(num_list) == 1:
        result = -1
