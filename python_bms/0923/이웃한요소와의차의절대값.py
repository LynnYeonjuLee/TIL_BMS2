import sys
sys.stdin = open("이웃한요소와의차의절대값.txt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
# 4 방향선언
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 2 for 문 순회


sum = 0
for x in range(N):
    for y in range(N):
        # 4방향 순회
        for i in range(4):
            # 방향 설정
            testX = x + dx[i]
            testY= y + dy[i]
            # 인덱스 체크
            if testX < 0 or testX >= N: continue
            if testY < 0 or testY >= N: continue
            # 할 일
            sum += abs(arr[x][y] - arr[testX][testY])
print(sum)