T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int,input().split())) for _ in range(N)]
    
    step = 0
    mid = N//2

    ans = 0

    for i in range(N):
        # 행을 순회하면서 행마다 열 인덱스 설정
        for j in range(mid-step, mid+step+1):
            ans += farm[i][j]
        if i < mid:
            step += 1
        else:
            step -= 1
    print('#{} {}'.format(tc, ans))
    
# 중앙을 기준으로 좌/우 순회 범위를 정해주기 
# 행이 늘어나면, 좌우 영역이 1씩 증가하다가
# 중앙선을 넘어서면 다시 좌우 영역이 1씩 감소한다. 

# 입력받고 

# 큰 반복은 N번 순회
# 그 안에서 왼쪽 범위부터 오른쪽 범위까지 돌면서 값을 더해주자. 
# 이때 행이 중앙을 넘지 않았다면 좌우가 증가 
# 중앙을 넘었다면 좌우가 감소 




# 두번째 방법 
# 어차피 중앙을 기준으로 위아래가 좌우 범위의 중복이 발생하므로 절발만 돌고도 구할 수 있다. 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int,input().split())) for _ in range(N)]


    row = N//2
    ans = 0
    for i in range(N):
        ans += farm[row][i]

    for i in range(1, N//2+1):
        st = 0 + i
        ed = N-1-i

        for j in range(st, ed+1):
            ans += farm[row+i][j] + farm[row-i][j]

    print('#{} {}'.format(tc, ans))