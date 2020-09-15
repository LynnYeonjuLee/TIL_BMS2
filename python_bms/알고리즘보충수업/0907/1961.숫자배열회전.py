T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = [input().split() for _ in range(N)]
    
    num_list.append(nums)
    result90 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(num_list[i][j])
        temp.reverse()
        result90.append(temp)
    result180 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(result90[i][j])
        temp.reverse()
        num_list.append(temp)
    result270 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(result180[i][j])
        temp.reverse()
        result270.append(temp)
    
    print('#{} {}'.format(tc))
    for i in range(n):
        print(''.join(list(map(str, result90[i]))), ''.join(list(map(str, result180[i]))), ''.join(list(map(str, result270[i]))))
            