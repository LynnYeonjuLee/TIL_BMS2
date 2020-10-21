n = list(map(int,input()))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cnt = 1
for i in n:
    if i in nums and i != 6 and i != 9:
        nums.remove(i)
    if i not in nums and i != 6 and i != 9:
        cnt += 1
        for j in range(1, 10):
            nums.append(i)
        nums.remove(i)
    if i == 6 and i in nums:
        nums.remove(i)
    if i == 6 and i not in nums and 9 in nums:
        nums.remove(9)
    if i == 6 and i not in nums and 9 not in nums:
        cnt += 1
        for j in range(1, 10):
            nums.append(i)
        nums.remove(6)
    if i == 9 and i in nums:
        nums.remove(i)
    if i == 9 and i not in nums and 6 in nums:
        nums.remove(6)
    if i == 9 and i not in nums and 6 not in nums:
        cnt += 1
        for j in range(1, 10):
            nums.append(i)
        nums.remove(9)
print(cnt)




