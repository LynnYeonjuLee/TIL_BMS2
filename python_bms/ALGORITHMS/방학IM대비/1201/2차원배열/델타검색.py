arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# for row in arr:
    # print(*row)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
N = len(arr)
M = len(arr[0])

# 모든 좌표에 대해서 델타 탐색하기
for r in range(N):
    for c in range(M):
        for k in ransge(4):
            nr = r + dr[k]
            nr = c + dc[k]
            if nr < or nr >= N or nc < 0 or nc >= M:
                continue
            else:
                print(arr[nr][nc], end=" ")
        print()