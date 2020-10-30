# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     agr_lst = []
#     for _ in range(N):
#         agr = list(map(int,input()))
#         agr_lst.append(agr)
#     # print(agr_lst)
#     sum_ = 0
#     for i in range(N): # 0 1 2 3 4 
#         for j in range(N): # 0 1 2 3 4 
#             if j == (N//2): # 정 가운데 행은 다 더해준다. 
#                 sum_ += agr_lst[j][i]
#             elif j < (N//2): # 정 가운데 행을 기준으로 위쪽 0 1 
#                 sum_ += agr_lst[j-(N//2)][i-(N//2)]
#             else: # 아래쪽 3 4
#                 pass
#                 # sum_ += agr_lst[j][i]
#     print(sum_)
T = int(input())
for t in range(1, T+1):
    N = int(input())
    agr_lst = []
    for _ in range(N):
        agr = list(map(int,input()))
        agr_lst.append(agr)
    # print(agr_lst)
    sum_ = 0
    step = 0
    mid = N // 2
    for i in range(N):
        for j in range(mid-step, mid+step+1):
            sum_ += agr_lst[i][j]
        if i < mid:
            step += 1
        else:
            step -= 1
    print('#{} {}'.format(t, sum_))