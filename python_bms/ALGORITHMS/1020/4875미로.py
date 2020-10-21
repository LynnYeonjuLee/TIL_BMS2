from collections import deque
# bfs 
dx = [0, 0, -1, 1] # 상하좌우 
dy = [-1, 1, 0, 0]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = []
    result = 0
    # visit_arr = [] # 내가 지나간 길을 채워줄 리스트
    for n in range(N):
        maze.append(list(map(int,input())))  # 입력 끝
        # print(maze)
    for i in range(N): # y!!!
        for j in range(N): # x!!!
            if maze[i][j] == 2:
                q = deque()
                q.append((i,j))
                # 지나간 부분은 상관없는 숫자 4 로 바꿔주기
                maze[i][j] = 4
    while q:
        q_pop = q.pop()
    # if maze[i][j] != 2:
    #     continue
        for k in range(4):
            nx = q_pop[1] + dx[k]
            ny = q_pop[0] + dy[k]
            # 1. 범위체크 
            if ny < 0 or nx < 0 or ny >= N or nx >= N: # 범위 주의하기 
                continue
            # 2. 못가는 길 패스해주기 
            if maze[ny][nx] == 1 or maze[ny][nx] == 4:
                continue
            # 0인 경우 
            if maze[ny][nx] == 0:
                q.append((ny,nx))
                # 지나간 부분은 상관없는 숫자 4 로 바꿔주기
                maze[ny][nx] = 4
            # 3. 3일 경우 길이 있다는 것 !
            if maze[ny][nx] == 3:
                result = 1
                break                             
                # # 이 부분이 틀린지 모르겠다... 훔 ..
                # i = ny
                # j = nx
    print('#{} {}'.format(t, result))
