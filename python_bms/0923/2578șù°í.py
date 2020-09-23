def linenum(bingo):
    line = 0
    # 1. 가로
    for i in range(5):
        cnt_zero = 0
        for j in range(5):
            if bingo[i][j] == 0:
                cnt_zero += 1
        if cnt_zero == 5:
            line += 1
    # 2. 세로
    for i in range(5):
        cnt_zero = 0
        for j in range(5):
            if bingo[j][i] == 0:
                cnt_zero += 1
        if cnt_zero == 5:
            line += 1
    # 3. 대각선1
    cnt_zero = 0
    for i in range(5):
        if bingo[i][i] == 0:
            cnt_zero += 1
    if cnt_zero == 5:
        line += 1

    # 4. 대각선2
    cnt_zero = 0
    for i in range(5):
        if bingo[4 - i][i] == 0:
            cnt_zero += 1
    if cnt_zero == 5:
        line += 1
    return line


bingo = [list(map(int,input().split())) for _ in range(5)]
bingo_ans2 = []
for _ in range(5):
    bingo_ans = list(map(int,input().split()))
    bingo_ans2 += bingo_ans
# print(bingo_ans2) ---> [5, 10, 7, 16, 2, 4, 22, 8, 17, 13, 3, 18, 1, 6, 25, 12, 19, 23, 14, 21, 11, 24, 9, 20, 15]
# print(bingo)
cnt = 0
for t in range(25):
    cnt += 1
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == bingo_ans2[t]:
                bingo[i][j] = 0
    line2 = linenum(bingo)
    if line2 >= 3:
        print(t+1)
        break
