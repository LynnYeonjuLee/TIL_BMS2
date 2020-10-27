def rotate90(nums_list):

    temp = [[-1] * N for i in range(N)]
    for r in range(Y-1,Y+K-1):
        for c in range(X-1,X+K-1):
            temp[c+1][Y-1+K-r] = nums_list[r][c]

    return temp
X , Y = 1 , 1
K = 4

N = 4
arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(rotate90(arr))