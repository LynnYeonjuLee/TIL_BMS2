'''
3 3
1 2 3
4 5 6
7 8 9
'''

# 첫번째 방법
N, M = map(int, input().split())
mylist = [0 for _ in range(N)]
#mylist = [0] * N

for i in range(N):
    mylist[i] = list(map(int,input().split()))
print(mylist)


# 두번째방법
N, M = map(int, input().split())
mylist = [0 for _ in range(N)]
for i in range(N):
    mylist.append(list(map(int,input().split()))
print(mylist)

# 세번째방법 -  간략해서 이걸 많이 쓴다.
N, M = map(int, input().split())
mylist = [list(map(int,input().split()))) for _ in range(N)]
print(mylist)

# 0으로 visited 초기화
# 1. 1차원
v = [0] * 3
print(v)

# 2. 2차원
N = 3 # 행
M = 4 # 열
v = [[0 for _ in range(N)] for _ in range(M)]
print(v)

# 아니면
v = [[0] * M for _ in range(N)]
print(v)





N, M = map(int, input().split())
mylist = [list(map(int,input().split()))) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)




arr = [1, 2, 3, 4]
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
    print((arr[i], arr[j]),end=' ')