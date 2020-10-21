move_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def iswall(y, x):
    if y < 0 or x < 0 or y >= N or x >= N:
        return True
    return False
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    y, x = 0, 0
    result = 0
    for i in range(N):
        if 2 in map_list[i]:
            x = map_list[i].index(2)
            y = i
            break
    stack = [(y, x)]
    while stack:
        temp_list = []
        y, x = stack.pop()
        map_list[y][x] = 1
        for _y, _x in move_list:
            dy = y + _y
            dx = x + _x
            if iswall(dy, dx):
                continue
            if map_list[dy][dx] == 3:
                result = 1
                break
            elif not map_list[dy][dx]:
                stack.append((dy, dx))
        else:
            continue
        break
    print('#{} {}'.format(tc, result))