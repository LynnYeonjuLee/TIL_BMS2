T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = []
    for i in range(N):
        nums.append(list(map(int,input().split())))
    # print(nums)
    result_arr = [[0]*N for _ in range(N)]
    # 90도 회전
    rotate90 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(nums[i][j])
        # print(temp)
        temp.reverse()
        # print(temp)
        rotate90.append(temp)
    rotate180 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(rotate90[i][j])
        temp.reverse()
        rotate180.append(temp)
    rotate270 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(rotate180[i][j])
        temp.reverse()
        rotate270.append(temp)
    print('#{}'.format(t))
    for i in range(N):
        print(''.join(list(map(str,rotate90[i]))),''.join(list(map(str,rotate180[i]))),''.join(list(map(str,rotate270[i]))))



