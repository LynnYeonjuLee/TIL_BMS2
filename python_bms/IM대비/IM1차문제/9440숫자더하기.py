nums = list(map(int,input().split()))
num_l1=[]
num_l2=[]
for i, v in enumerate(nums):
    
while len(nums) > 0:
    num_l1.append(min(nums))
    nums.remove(min(nums))
    num_l2.append(min(nums))
    nums.remove(min(nums))
print(num_l1)
print(num_l2)
