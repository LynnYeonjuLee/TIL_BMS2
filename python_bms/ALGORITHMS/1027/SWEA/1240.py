# def check(nums_list):
#     for i in range(M//7):
#         if nums_list
T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    nums_list = []
    for n in range(N):
        nums = list(map(int,input().split()))
        nums_list.append(nums)
        nums_list = nums[0:M:7]
        print(nums_list)
    for i in range(N):
        pass
    # print(nums_list)