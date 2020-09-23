N = int(input())
P =[0 for i in range(1001)]
# print(P)
max1 = 0
idx = 0
start_idx = 0
end_idx = 0
idx_list = []
for n in range(N):
    a, b =map(int, input().split())
    P[a] = b

    if max1 < b:
        max1 = b
        idx = a
    idx_list.append(a)
    idx_list.sort()
    start = min(idx_list) # idx_list[0]
    end = max(idx_list) #idx_list[-1]


    sum = 0
    value = 0 #  왼쪽에서 가면서 최대의 값
     # 왼쪽 사각형 넓이 구하기
    for i in range(start, idx):
        value = max(value, P[i])
        sum += value
    # 오른쪽 사각형 넓이 구하기
    value = 0
    for i in range(end, idx, -1):
        value = max(value, P[i])
        sum += value
    sum += max1

print(sum)