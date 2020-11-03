# 시간초과 

N, K = map(int,input().split())
tems = list(map(int,input().split()))
sum_list = []

# for i in range(N-K+1):
#     sum1 = 0
#     for k in range(i, i+K):
#         sum1 += tems[k]
#     sum_list.append(sum1)
# result = 0
# for sum_ in sum_list:
#     if sum_ > result:
#         result = sum_
# print(result)
sum_ = 0
temp = []
for i in range(K):
    temp.append(tems[i])
    sum_ += tems[i]
sum_list.append(sum_)

for i in range(K, N-K+2):
    temp.remove(temp[0])
    temp.append(tems[i])
    sum_list.append(sum(temp))
print(max(sum_list))
# print(sum_list)