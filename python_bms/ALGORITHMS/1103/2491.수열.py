# 런타임에러
N = int(input())
nums = list(map(int, input().split()))
compare_in = nums[0]
compare_de = nums[0]
length_in = 1
length_de = 1
result = []
for i in range(1, len(nums)):
    if nums[i] >= compare_in:
        compare_in = nums[i]
        length_in += 1
        result.append(length_in)
    else:
        compare_in = nums[i]
        length_in = 1

for i in range(1, len(nums)):
    if nums[i] <= compare_de:
        compare_de = nums[i]
        length_de += 1
        result.append(length_de)
    else:
        compare_de = nums[i]
        length_de = 1

# result2 = max(result)
if len(nums) == 1:
    print(1)
elif max(result) < 3:
    print(2)
else:
    print(max(result))
# if length_in >= length_de:
#     print(length_in)
# else:
#     print(length_de)
# print(max(result))