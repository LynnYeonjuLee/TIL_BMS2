W, H = map(int,input().split())
N = int(input())
store = list(map(int,input().split()))
dong = list(map(int,input().split()))

def calD(dir,dist): # 기준점(상좌) 을 기준으로 한 거리 구하는 함수
    # 북남서
    if dir == 1:
        return dist
    elif dir == 2:
        return W + H + (W - dist)
    elif dir == 3:
        return W + H + W + (H - dist)
    else:
        return W + dist

# 기준점 - 상점, 기준점 - 동근 거리를 구하고 둘을 빼면 둘의 거리차
d1 = calD(dong[0], dong[1]) # 동근이 거리 계산
total = 0 # 최단 거리 누적
for i in range(N): # 상점들의 거리 계산
    d2 = calD(store[i][0], store[i][1])
    # 경로1 : 기준점-상점, 기준점 - 동근 거리 구하고 둘을 빼면 둘의 거리 차이
    p1 = abs(d1-d2)
    # 경로2: 전체 둘레 - 경로1
    p2 = 2*(W+H) - p1
    if p1 < p2:
        total += p1
    else:
        total += p2
print(total )