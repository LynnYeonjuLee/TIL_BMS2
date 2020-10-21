def dfs(idx):
    global count
    count += 1
    for i in Tree[idx]:
        dfs(i)
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tmp = input().split()
    Tree = [ [ ] for _ in range(E+2)]
    for idx, i in enumerate(range(0, E*2, 2)):
        a = int(tmp[i])
        b = int(tmp[i+1])
        Tree[a].append(b)    
    count = 0
    dfs(N)
    print('#{} {}'.format(tc, count))