N = int(input())
nums = list(map(int,input().split()))
new_nums = sorted(nums)
print(new_nums[N//2])