from itertools import product
N, M = map(int,input().split())
nums = []
for n in range(1, N+1):
    nums.append(n)
# print(nums)
result = []
for num in product(nums, repeat = M):
    for i in num:
        print(i,end=" ")
    print(end='\n')



# for i in range(len(result)):
#     a = result[i]
#     for j in range(len(a)):
#         print(a[j])
# for i in range(len(result)):
#     for j in range(M):
#         print(result[j])
# 이차원으로 바로 찍어도 되겠지 ! 