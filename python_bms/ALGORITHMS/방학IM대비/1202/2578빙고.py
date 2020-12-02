def line_num(bingo):
    line = 0
    # 가로
    for i in range(5):
        cnt_zero = 0
        for j in range(5):
            if bingo[i][j] == 0:
                cnt_zero += 1
        if cnt_zero == 5:
            line += 1
    # 세로
    for i in range(5):
        cnt_zero = 0
        for j in range(5):
            if bingo[j][i] == 0:
                cnt_zero += 1
        if cnt_zero == 5:
            line += 1
    # 대각선 1
    cnt_zero = 0
    for i in range(5):
        if bingo[i][i] == 0:
            cnt_zero += 1
    if cnt_zero == 5:
        line += 1
    # 대각선 2
    cnt_zero = 0
    for i in range(5):
        if bingo[4 - i][i] == 0:
            cnt_zero += 1
    if cnt_zero == 5:
        line += 1
    return line
# 25개 칸 5*5
bingo = [list(map(int,input().split())) for _ in range(5)]
bingo_ans2 = []

cnt = 0
for _ in range(5):
    bingo_ans = list(map(int,input().split()))
    bingo_ans2 += bingo_ans
# print(bingo_ans2)
for a in range(25):
    cnt += 1
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == bingo_ans2[a]:
                bingo[i][j] = 0
    line_ans = line_num(bingo)
    if line_ans >= 3:
        print(cnt)
        break







# bingo_ans = [list(map(int,input().split())) for _ in range(5)]
# print(bingo)
# print(bingo_ans)
#cnt_zero = 0
# cnt = 0
# cnt_ans = 0
# for i in range(5):
#     for j in range(5):
#         for k in range(5):
#             for m in range(5):
#                 # 사회자가 부르는 수를 0으로 바꿔주자
#                 if bingo_ans[i][j] == bingo[k][m]:
#                     bingo[k][m] = 0
#                     cnt_ans += 1
#                 if bingo[k][m] == 0:
#                     cnt_zero += 1
#             if cnt_zero == 5:
#                 cnt += 1
#         if cnt >= 3:
#             break
# print(cnt_ans)

cnt = 0
# for t in range(25)




        # print(bingo)
        # 가로 체크
        # for n in range(5):
        #     for k in range(n):
        #         for m in range(5):
        # 세로 체크
        # 대각선 체크
# 가로줄 세로줄 또는 대각선 위에 있는 5개 수가 0이되면 선을 긋는다

# 세 개 이상인 순간 빙고를 외치는데
# 가장 먼저 외치는 사람이 게임의 승자
