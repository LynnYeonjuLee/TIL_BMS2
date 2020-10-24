def rotation(nums):
    # 원하는 배열의 크기만큼 만들어놓고 
    tmp = [['']*N for i in range(N)]
    # 회전 
    for i in range(N):
        for j in range(N):
            tmp[j][N-1-i] = nums[i][j]
    return tmp

def result(nums, col):
    for i in range(N):
        for j in range(N):
            # 문자열 + 문자열 = 문자열이니까 
            ans[i][col] += nums[i][j]


T = int(input())
for t in range(1, T+1):
    N = int(input())

    arr = [input().split() for _ in range(N)]
    # 나중에 출력을 편하게 하기 위해 그냥 문자 상태로 받았다. 
    # for i in arr: 
        # print(*i)
    # 3개의 의미는 각각 90도 180도 270도 
    ans = [['']*3 for _ in range(N)]

    for i in range(3):
        arr = rotation(arr)
        result(arr,i)
    
    print('#{}'.format(t))
    for i in range(N):
        for j in range(N):
            print(ans[i][j], end=' ')
            print()
    
# 회전에 백준17406