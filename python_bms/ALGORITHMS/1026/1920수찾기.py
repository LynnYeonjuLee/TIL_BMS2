N = int(input())
nums = set(map(int,input().split()))
M = int(input())
nums2 = list(map(int,input().split()))
for num in nums2:
    if num in nums:
        print(1)
    else:
        print(0)