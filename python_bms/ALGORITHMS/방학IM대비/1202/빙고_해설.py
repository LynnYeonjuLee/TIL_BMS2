bingo = [list(map(int,input().split()))for _ in range(5)]
call = [list(map(int,input().split())) for _ in range(5)]
# print(bingo)
# print(call)

def check():# 가로, 세로, 대각선 에 0 로 이뤄진 선이 있는지 확인
    lcnt = 0 # 라인의 수
    for i in range(5):
        cnt = 0 # 0의 개수
        while bingo[i][j] == 0:

        # for j in range(5):
        #     if bingo[i][j] == 0:
        #         cnt += 1
        # if cnt == 5:
        #     lcnt += 1

    # for i in range(5):
    #     cnt = 0
    #     for j in range(5):
    #         if bingo[j][i] == 0:
    #             cnt += 1
    #     if cnt == 5:
    #         lcnt += 1
    # cnt = 0
    # for i in range(5):
    #     if bingo[i][i] == 0:
    #         cnt += 1
    # if cnt == 5:
    #     lcnt += 1
    #
    # cnt = 0
    # for i in range(5):
    #     if bingo[4-i][i] == 0:
    #         cnt += 1
    # if cnt == 5:
    #     lcnt += 1


isBingo = False # 빙고인지 아닌지를 저장
n_cnt = 0 # 숫자를 외치는 횟수
for i in range(5):
    for j in range(5):
        # print(call[i][j])
        n_cnt += 1
        for k in range(5):
            for m in range(5):
                if bingo[k][m] == call[i][j]:
                    bingo[k][m] = 0
        check()