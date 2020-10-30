T = int(input())
for t in range(1, T+1):
    N = int(input())
    if N == 1:
        print('#{}'.format(t))
        print(1)
    elif N == 2:
        print('#{}'.format(t))
        print(1)
        result = [1, 1]
        for x in range(2):
            print(result[x],end=' ')
        print()
    else:
        arr1 = [1]
        arr2 = [1, 1]
        result = []
        result.append(arr1)
        result.append(arr2)
        start = 2
        temp = []
        while len(temp) != N:

            # for n in range(len(arr2)):
                # for a in range()
            temp = [0]*start
            temp[0] = 1
                # for i in range(len(arr2)):
            for a in range(1, start):
                temp[a] = arr2[a] + arr2[a-1]
                # temp[]
                # temp.append(1)
            temp.append(1)
            start += 1
            result.append(temp)
            arr2 = temp
        
        print('#{}'.format(t))
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j], end=' ')
            print()

    # print(result)
