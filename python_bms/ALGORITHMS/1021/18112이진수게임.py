from collections import deque
start = int(input())
goal = int(input())
idx = 0
start_sum = 0
goal_sum = 0
while(start):
    start_sum += (start%10) * (1<<idx)
    idx += 1
    start //= 10
# start_int = sum
idx = 0
while(goal):
    goal_sum += (goal%10) * (1<<idx)
    idx += 1
    goal //= 10
# print(goal_sum)
# print(start_sum)
# goal_int = sum
# bfs 를 돌려서 바꿀 수 있는 경우를 전부 바꿔서 확인하고 맞으면 정지.
# bfs 를 돌다가 원하는 수를 찾았다. 그럼 종료 

#   queue에 정수와 거리값을 넣어둔다. 
q = deque()
q.append((start_sum,0))
visited = [False] * 10000
result = 0
visited[start_sum] = True

while q:
    b = q.popleft()
    if b[0] == goal_sum:
        result = b[1]
        break
    i = 0
    while b[0] >= (1 << i):
        i += 1
    i -= 1
    # print(1 << i)

    # 조건 1 
    new_b = 0
    for idx in range(i-1, -1, -1):
        if (b[0] & (1 << idx)) > 0:
            new_b = b[0] - (1 << idx)
        else:
            new_b = b[0] + (1 << idx)
        if new_b < 0 or new_b > 5000:
            continue
        if visited[new_b]:
            continue
        visited[new_b] = True
        q.append((new_b, b[1] + 1))
    # new_b = 0
    # 조건 2, 3
    for i in range(2):
        # 조건 2
        if i == 0 and b[0] < 4999:
            new_b = b[0] + 1
        # 조건 3
        elif i == 1 and b[0] != 0:
            new_b = b[0] - 1
        else:
            continue
        if visited[new_b]:
            continue
        
        visited[new_b] = True
        
        q.append((new_b, b[1]+1))
print(result)