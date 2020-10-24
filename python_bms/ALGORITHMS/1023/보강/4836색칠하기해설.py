def paint(r1,c1,r2,c2,color):
    # global ans
    cnt = 0
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            arr[i][j] += color
            if arr[i][j] == 3:
                cnt += 1
                # ans += 1 
    return cnt # ans 를 쓸 땐 얘 빼고 

for tc in range(1, int(input())+1):
    N = int(input())
    # print(N)

    arr = [[0] * 10 for _ in range(10)]
    cnt = 0
    for i in range(N):
        # 왼쪽 모서리 좌표, 오른쪽 모서리 좌표, 색깔 
        r1, c1, r2, c2, color = map(int,input().split())
        ans += paint(r1, c1, r2, c2, color)  # 함수 안에서 글로벌 ans 선언해주면 paint 만 써두 된다.
    print('#{} {}'.format(tc,cnt))