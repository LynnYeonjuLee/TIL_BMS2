from collections import deque
dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

while(True):
    x, y = list(map(int,input().split()))
    
    if x == 0 and y == 0:
        break 
    arr = []
    cnt = 0
    for i in range(y):
        arr.append(list(map(int,input().split())))
    for i in range(y):
        for j in range(x):
            if arr[i][j] == 1:
                q = deque()
                q.append((i, j))
                arr[i][j] = 2
                while q: # q 안에 있는 원소들이 끝날 때까지 계속 돈다. 
                    q_pop = q.pop()
                    for k in range(8):
                        nx = q_pop[1] + dx[k]
                        ny = q_pop[0] + dy[k]
                        # 범위를 벗어나는 부분은 그냥 통과 => 1. 범위 체크
                        if ny < 0  or nx < 0 or ny >= y or nx >= x:
                            continue
                        if arr[ny][nx] != 1: # 2. visit 체크
                            continue
                        q.append((ny, nx)) # 3. q에 추가하면서 visit 변경
                        arr[ny][nx] = 2
                cnt += 1       

    print(cnt)
                        


        