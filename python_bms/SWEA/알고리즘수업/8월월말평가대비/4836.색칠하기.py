def color(x1, y1, x2, y2, c, arr):
    for y in range(y1, y2+1):
        for x in range(x1, x2+1):
            if c == 1:
                arr[y][x] += 1
            if c == 2:
                arr[y][x] += 2



T = int(input())
for tc in range(1, T+1):
    arr = [[0]*10 for _ in range(10)]
    N = int(input())
    nums_info = []
    for i in range(N):
        nums = list(map(int,input().split()))
        nums_info.append(nums)

    for nums in nums_info:
        color(nums[0], nums[1], nums[2], nums[3], nums[4], arr)

    cnt = 0
    for i in arr:
        for j in i:
            if j == 3:
                cnt += 1

    print('#{} {}'.format(tc, cnt))




# def color(x1, y1, x2, y2, c, arr):
#     for y in range(y1, y2+1):
#         for x in range(x1, x2+1):
#             if c == 1:
#                 arr[y][x] += 1
#             if c == 2:
#                 arr[y][x] += 2

# T = int(input())


# for test_case in range(1, T+1):
#     arr = [[0] * 10 for _ in range(10)]

#     N = int(input())
#     square_info = []
#     for i in range(N):
#         square = list(map(int,input().split()))
#         square_info.append(square)

#     for square in square_info:
#         color(square[0], square[1], square[2], square[3], square[4], arr) 
#         # 받은 사각형 정보를 통해 arr 에 숫자를 바꿔줬음 -> 그 숫자 중 3인 것을 찾자 
#     # print(arr)

#     cnt = 0
#     for i in arr:
#         for j in i:
#             if j == 3:
#                 cnt += 1
    


     

#     print(f'#{test_case} {cnt}')