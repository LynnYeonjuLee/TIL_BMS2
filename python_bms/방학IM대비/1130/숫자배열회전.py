def rotate(N, arr):
    new_li = []
    for i in range(N):
        temp = []
        for j in range(N-1,-1,-1):
            temp.append(arr[j][i])
        new_li.append(temp)
    return new_li
T = int(input())
for t in range(1, T+1):
    N = int(input())
    list1 = []
    for i in range(N):
        list1.append(list(map(int,input().split())))
    l_90 = rotate(N,list1)
    l_180 = rotate(N,l_90)
    l_270 = rotate(N,l_180)
    result_list = [l_90,l_180,l_270]
    print('#{}'.format(t))
    for i in range(N):
        for j in range(3):
            print(''.join(map(str,result_list[j][i])),end=' ')
        print()
