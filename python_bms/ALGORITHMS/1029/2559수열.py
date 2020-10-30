N, K = map(int,input().split())
tems = list(map(int,input().split()))
sum_list = []
for i in range(N-K+1):
    sum1 = 0
    for k in range(i, i+K):
        sum1 += tems[k]
    sum_list.append(sum1)
result = 0
for sum_ in sum_list:
    if sum_ > result:
        result = sum_
print(result)
# print(max(sum_list))