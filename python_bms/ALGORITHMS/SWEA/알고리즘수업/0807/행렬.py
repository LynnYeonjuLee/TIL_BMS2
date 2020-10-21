def side(i, j):
    count = 1
    dx = j
    while True:
        dx += 1
        if dx >= N: 
            break
        if map_list[i][dx]: count+=1
        else: 
            break
    return cnt

def down(i, j):
    count = 1
    dy = i
    while True:
        dy += 1
        if dy >= N: 
            break
        if map_list[dy][j]: count+=1
        else: 
            break
    return cnt
 
def change(y1, x1, y2, x2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            map_list[i][j] = 0
 
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, input().split())) for _ in range(N)]
    result_list = []
    for i in range(N):
        for j in range(N):
            if map_list[i][j]:
                s = side(i, j)
                d = down(i, j)
                change(i, j, i+d, j+s)
                result_list.append([d, s, d*s])
    result_list = sorted(result_list, key=lambda x: (x[2], x[0]))
    #lambda 부분 블로그 참조함
    print('#{} {}'.format(test_case, len(result_list)), end= ' ')
    for r, c, _ in result_list:
        print('{} {}'.format(r, c), end=' ')
    print()