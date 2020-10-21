nums = list(map(int,input()))
cnt = 1
num_l = []
nines_cnt = 0
nines = []
for i in range(len(nums)):
    if nums[i] not in num_l and nums[i] != 6 and nums[i] != 9: 
        num_l.append(nums[i])
    elif nums[i] == 6 or nums[i] == 9:
        nines.append(9)
    elif nums[i] in num_l:
        cnt += 1
if nines.count(9) % 2 == 1:
    if nines.count(9) == 1:
        nines_cnt += 0
    else:
        nines_cnt += (nines.count(9) // 2 + 1)
else: 
    nines_cnt += nines.count(9) // 2
if len(num_l) == 0:
    cnt = 0
else: 
    pass
print(cnt+nines_cnt)
