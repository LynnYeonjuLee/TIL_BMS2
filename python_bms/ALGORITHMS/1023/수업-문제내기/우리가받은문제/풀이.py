T = int(input())
for t in range(1, T+1):
    L, K, M, KN= list(map(int,input().split()))
    # L 회전시킬 자석위치 K 회전수 M 자석개수 KN 톱니개수
    magnet = [list(map(int, input().split())) for _ in range(M)]
    for _ in range(abs(K)):
        i, rot = L, K // abs(K)
        i -= 1  
        move = [(i, rot)] 
        temp = rot
        for a in range(i - 1, -1, -1):
            if magnet[a][KN*1//4] != magnet[a + 1][KN*3//4]:
                temp *= -1
                move.append((a, temp))
            else:
                break
        temp = rot
        for a in range(i + 1, M):
            if magnet[a][KN*3//4] != magnet[a - 1][KN*1//4]:
                temp *= -1
                move.append((a, temp))
            else:
                break
        for i, rot in move:
            if rot == 1:
                magnet[i] = [magnet[i].pop()] + magnet[i]
            elif rot == -1:
                magnet[i].append(magnet[i].pop(0))
    result = 0
    for i in range(M):
        result += magnet[i][0] * 2**i

    print('#{} {}'.format(t, result))