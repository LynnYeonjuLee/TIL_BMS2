# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
# 인접행렬과 인접리스트를 받아오자.
N, E = list(map(int,input().split()))
temp == list(map(int,input().split()))
adj_arr = [[0]*(N+1) for _ in range(N+1)]
for i in range(0, len(temp), 2):
    adj_arr[temp[i]][temp[i+1]] = adj_arr[temp[i+1]][temp[i]] = 1
for i in adj_arr:
    print(i)


# 두 가지 방법 !



# 인접리스트
# T = int(input())
# for t in range(1, T+1):
#     N, K = list(map(int,input().split()))
#     for i in range(N):
#         nums = list(map(int,input()))
Garr = [[-1 for _ in range(8)] for _ in range(8)]
Glist = [[] for _ in range(8)]
inval = list(map(int,input().split()))
for i in range(len(inval)//2):
    val1 = inval[i*2]
    val2 = inval[i*2+1]
    Garr[val1][val2] = 1
    Garr[var2][var1] = 1

    Glist[val1].append(val2)
    Glist[val2].append(val1)
print(Garr)
print(Glist)