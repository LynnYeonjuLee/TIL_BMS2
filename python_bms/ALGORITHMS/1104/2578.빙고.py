# 아아아아아아아아아아아아아악 미완성
bingo = []
ans = []
for _ in range(5):
    b = list(map(int,input().split()))
    bingo.append(b)
for _ in range(5):
    b2 = list(map(int,input().split()))
    ans.append(b2)
# print(bingo)
# print(ans)
ans2 = []
for i in range(5):
    for j in range(5):
        ans2.append(ans[i][j])
print(ans2)
cnt = 0
bing = 0
ans_sheet = [[0]*5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        for k in range(len(ans2)):
        #     for l in range(5):
            if bingo[i][j] == ans2[k]:
                cnt += 1
                ans_sheet[i][j] = -1
                for l in range(5):
                    cnt_minus = 0
                    for m in range(5):
                        if ans_sheet[l][m] == -1:
                            cnt_minus += 1
                            if cnt_minus == 5:
                                bingo += 1
                        elif ans_sheet[m][l] == -1:
                            cnt_minus += 1
                            if cnt_minus == 5:
                                bingo += 1
                        elif 
                            bingo += 1
                        else: bingo += 1
print(ans_sheet)