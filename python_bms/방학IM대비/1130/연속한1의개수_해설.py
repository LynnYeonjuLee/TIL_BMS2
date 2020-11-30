T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(input())
    i = 0 # 반복계수
    dist = 0 # 1의 개수 카운팅
    max = 0
    while i < N:
        num = int(arr[i]) # 현위치의 숫자
        if dist == 0 and num == 1: # 1을 처음 만나면
            dist = 1
        elif dist > 0 and num == 1: # 만난적이 있고 나도 1이고
            dist += 1
        elif num == 0: # 수가 0이면 카운팅은 리셋
            dist = 0
        if max < dist:
            max = dist
        i += 1
    orint('#{} {}'.format(t, max))