T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = []
    for _ in range(N):
        nums = list(map(int,input().split()))
        num_list.append(nums)
        
    turn90 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(num_list[i][j])
        temp.reverse()
        turn90.append(temp)

    turn180 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(turn90[i][j])
        temp.reverse()
        num_list.append(temp)

    turn270 = []
    for j in range(N):
        temp = []
        for i in range(N):
            temp.append(turn180[i][j])
        temp.reverse()
        turn270.append(temp)
    
    print('#{} {}'.format(t))
    for i in range(n):
        print(''.join(list(map(str, result90[i]))), ''.join(list(map(str, result180[i]))), ''.join(list(map(str, result270[i]))))
            