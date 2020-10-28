T = int(input())
for t in range(1, T+1):
    result = 0
    N = int(input())
    nums = list(map(int,input().split())
    result = max(nums) - min(nums)
print('#{} {}'.format(t,result))