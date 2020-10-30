N = int(input())
nums = []
for n in range(1, N+1):
    nums.append(str(n))
print(nums)
result = []
for i in range(len(nums)):
    cnt = 0
    if '3' in nums[i] or '6' in nums[i] or '9' in nums[i]:
        cnt += nums[i].count('3')
        cnt += nums[i].count('6')
        cnt += nums[i].count('9')
        # for c in range(cnt):
        # print('-')
            # result.append('-')
        print('-'*cnt, end=' ')
    else:
#         # print(nums[i])
            print(nums[i], end=' ')
#         result.append(nums[i])
# for i in range(len(result)):
#     if result[i] != '-':
#         print(result[i], end=' ')
#     else:
#         print(result[i], end=' ') # -얘만 붙여서 프린트를 어떻게 하쥥..
# # print(result)