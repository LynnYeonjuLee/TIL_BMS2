# 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 모든 출발점을 검사하여 가장 짧은 이동 거리를 갖는 시작점 x(복수 개인 경우 가장 큰 x좌표)를 반환하는 코드를 작성하라.(
    T = 10
for tc in range(1, T+1):
    test = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    min_count = 10000
    return_x = 0
    start_list = [i for i in range(99, -1, -1) if ladder[0][i]]
    for start in start_list:
        d_y = 0
        d_x = start
        count = 0
        move = 0
        down = 0
        left = 1
        right = 2
        while d_y < 99:
            if (move == down or move == left) and d_x > 0 and ladder[d_y][d_x-1]:
                d_x -= 1
                move = left
            elif (move == down or move == right) and d_x < 99 and ladder[d_y][d_x+1]:
                d_x += 1
                move = right
            elif ladder[d_y + 1][d_x]:
                d_y += 1
                move = down
            count +=1
        if min_count > count: 
            min_count = count
            return_x = start
    print("#{} {}".format(test, return_x))