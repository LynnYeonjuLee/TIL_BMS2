move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs():
    global q
    count = 0
    while q:
        snd_q = []
        while q:
            y,x = q.pop()
            for i, j in move:
                dy = y+i
                dx = x+j
                if 0 <= dy < N and 0 <= dx < N:
                    if not map_list[dy][dx]:
                        map_list[dy][dx] = 1
                        snd_q.append((dy, dx))
                    if map_list[dy][dx] == 3:
                        return count
        count += 1
        q = snd_q
    return 0
 
for tc in range(1, 1+int(input())):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == 2:
                q.append((i, j))
                break
        else: continue
        break
    print('#{} {}'.format(tc, bfs()))