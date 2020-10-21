# 입력으로 9 X 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0 을 출력한다.
def sudoku_game(lst1,lst2,sudoku):
    result = 1
    s = [0 for _ in range(9)]
    for i in lst1:
        for j in lst2:
            s[sudoku[i][j]-1] += 1

    if max(s)!= 1 or min(s) != 1:
        result = 0
    return result

T = int(input())


for test_case in range(1, T+1):
    result = 1
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int,input().split())))
    for i in range(9):
        s = [0 for _ in range(9)]
        for j in range(9):
            s[sudoku[i][j]-1] += 1
            s[sudoku[j][i]-1] += 1
        if max(s)!= 2 or min(s)!= 2:
            result = 0
            break
    x = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for i in range(3):
        for j in range(3):
            if sudoku_game(x[i],x[j],sudoku) == 0:
                result = 0
                break
        if result == 0:
            break

    print(f'#{test_case} {result}')
    