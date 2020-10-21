# sorting 으로 문제를 푸는 것도 좋지만 다른 방법을 사용해보겠다! 
# 이 중에 제일 작은 것을 뽑는데 앞에 뽑았던거 보다는 큰 것 중에 제일 작은 것을 뽑자 
# 원본배열과 목표배열 2개 


# def
def getMin(curV):
    입력받은 scr 에서 curV보다 큰 값 중에 가장 작은 값을 구해서 리턴
    minV = 10000000
    for i in range(5):
        for j in range(5):
            if minV > src[i][j] and src[i][j] > curV:
                minV = src[i][j]

def isWall(X, Y):
    진짜, 
    이미 dst[Y][X]인 경우에도:

    if X<0 or X>=5:
        return True
    if Y <0 or Y>=5:
        return True
    if dst[y][x] != 0:
        return True
    return False


#src에 입력 

#dst 배열을 0으로 초기화 
dst = [[0] * 5] for _ in range(5)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dir = 0 # 0->1->2->3->0

cur X = curY = 0
curV = 0
for i in range(25):
    val = getMin(curV)
    dst[curY][curX] = val
    testX = curX + dx[dir]
    testY = curY + dy[dir]

    if isWall(testX, testY):

        # dir = dir+1
        # if dir == 4:
        #     dir = 0
        dir = (dir+1)%4
    curX = curX + dx[dir]
    curY = curY + dy[dir]
print(dst)
    위치계산 