def dfsr(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 9, 0]
    maze[newY][newX] = -1
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[j]
        if isWall() == True:
            continue
        if maze[newY][newX] == 3:
            return 1
        if maze[newY][newX] != -1 and maze[newY][newX] == 0: 
                dfsr(newX, newY)
    return 0
    




# 1. 입력을 받는다
T = int(input())
for t in range(1, T+1):
    # 1. 입력을 받는다. 
    N = int(input())
    # maze = list(map(int,input()))

    maze = [[int(x) for x in input() for _ in range(N)]]
    # 2. 시작점을 찾는다.
    # n_arr = []  시작점이 여기서는 하나지만 여러개인 문제에서는 담아주자. 
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                # n_arr.append((j,i)) 여러개
                nx = j 
                ny = i

    # 3. 재귀를 호출한다.  
    #for (nx,ny) in range(n_arr)여러개
    if dfsr(nx, ny) == 1:
        print(1)
    else:
        print(0)
# 4. 재귀함수를 만든다.
#       중간에 찾은 경우 1을 return 못찾은 경우 0을 return 한다.