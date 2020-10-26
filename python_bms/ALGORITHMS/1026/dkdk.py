def rotate90(nums_list):

    temp = [[-1] * N for i in range(N)]
    # 배열의 크기 K 

    # if (C//90)%4 == 1: # 90도
    # if (C//90)%4 == 1:
    for r in range(Y-1,Y+K-1):
        for c in range(X-1,X+K-1):
            temp[c+1][X+K-r] = nums_list[r][c]
    # elif (C//90)%4 == 2: # 180
    #     for r in range(Y-1,Y+K-1):
    #         for c in range(X-1,X+K-1):
    #             temp[N-r+1][N-c-1] = nums_list[r][c]

    # elif (C//90)%4 == 3: # 270
    #     for r in range(Y-1,Y+K-1):
    #         for c in range(X-1,X+K-1):
    #             temp[c+1][X+K-r] = nums_list[r][c]
    # else: # 360 
    #     for r in range(N):
    #         for c in range(N):
    #             temp[r][c] = nums_list[r][c]
    return temp

T = int(input())
for t in range(1, T+1):
    N, C, X, Y, K, R = list(map(int,input().split()))
    nums_list = []
    arr = []
    for _ in range(N):
        nums = list(map(int,input().split()))
        nums_list.append(nums)
        arr.append(nums)
    if X+K-1 > N or Y+K-1 > N:
        result = -1
    else:
        # 새로운 배열을 저장하자
        # temp1 = [[''] * K for i in range(K)]
        # for r in range(Y-1,Y+K-1):
        #     for c in range(X-1,X+K-1):
        #         print(r)
        #         print(c)
        #         # temp1[c-X+1][r-Y+1] = nums_list[c][r]
        #         temp1[r-Y+1][c-X+1] = nums_list[r][c]
        if (C//90)%4 == 1:
            nums_list = rotate90(nums_list)
        elif (C//90)%4 == 2: # 180
            nums_list = rotate90(nums_list)
            nums_list = rotate90(nums_list)
        elif (C//90)%4 == 3: # 270  
            nums_list = rotate90(nums_list)
            nums_list = rotate90(nums_list)
            nums_list = rotate90(nums_list)
        else: # 360 
            continue
       
        # result(nums_list,i)
        # for i in range(N):
        #     for j in range(N):
        #         if i <=
    
        # result_arr = []
        # for r in range(N):
        #     for c in range(N):
        #         if Y-1 <= r < Y+K-1 and X-1 <= c < X+K-1:
        #             result_arr[r][c] = temp[r][c]
        #         else:
        #             result_arr[r][c] = nums_list[r][c]



        # result_arr = []
        for r in range(N):
            for c in range(N):
                if nums_list[r][c] == -1:
                    nums_list[r][c] = arr[r][c]
                else:
                    continue
        # print(result_arr)
        result = 0
        for i in range(N):
            result += nums_list[R-1][i]
    print('#{} {}'.format(t,result))



    # for nums in nums_list:
    #     print(nums)

    
    '''
    1
    5 90 2 3 3 3
    1 2 3 4 5
    6 7 8 9 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25
    
    1
    5 270 2 3 3 3
    1 2 3 4 5
    6 7 8 9 10
    11 12 13 14 15
    16 17 18 19 20
    21 22 23 24 25
    '''


    
    