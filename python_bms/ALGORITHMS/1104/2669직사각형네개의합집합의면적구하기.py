sq = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    # sq.append(nums)
    
    for i in range(x1, x2):
        for j in range(y1,y2):
            if sq[i][j] == 0:
                sq[i][j] = 1
                cnt += 1
    # for i in range(100):
    #     for j in range(100):
    #         if sq[i][j] == 1:
    #             cnt +
print(cnt)