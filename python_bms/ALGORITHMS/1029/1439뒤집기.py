nums = list(map(int,input()))
# 0과 1을 뒤집는데 
# 0을 뒤집
# while 1 in nums and 0 in nums:
    
# # cnt0 = nums.count(0)
# # cnt1 = nums.count(1)
# # for i in range(len(nums)):
# #     if cnt0 >= cnt1:
# #         cnt_r = 0
# #         # 0의 개수가 더 많으면 1을 flip 해준다. 
# #         if nums[i] == 1:
# #             cnt_r += 1 # 를 하면 연속된 수는 확인할 수 없...으,,
# #     else:
# #         cnt_r = 0
# #         # 1의 개수가 더 많으면 0을 flip 해준다.
cnt = 0
for i in range(len(nums)-1):
    if nums[i] != nums[i+1]:
        cnt += 1
if cnt % 2 == 0:
    cnt = cnt 
else: 
    cnt += 1
print(cnt//2)