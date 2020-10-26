def rotate90(nums_list):

    temp = [[-1] * N for i in range(N)]
    for r in range(Y-1,Y+K-1):
        for c in range(X-1,X+K-1):
            temp[c+1][X+K-r] = nums_list[r][c]

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

        for r in range(N):
            for c in range(N):
                if nums_list[r][c] == -1:
                    nums_list[r][c] = arr[r][c]
                else:
                    continue
        result = 0
        for i in range(N):
            result += nums_list[R-1][i]
    print('#{} {}'.format(t,result))

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


    
    