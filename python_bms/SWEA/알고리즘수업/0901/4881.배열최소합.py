def dfs(idx, sum1):
    global result
    if idx == N:
        if sum1 < result:
            result = sum1
        return
    if sum1 >= result:
        return
    for i in range(N):
        if visited[i]:
            visited[i] = False
            dfs(idx+1, sum1 + lst[idx][i])
            visited[i] = True
    
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [True for _ in range(N)]
    result = 987654321
    dfs(0, 0)
    print("#{} {}".format(tc, result))