T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = input() # 입력에 사이공간이 없으니까 split을 안해준다.
    temp = []
    for card in cards:
        temp.append(card) 
    count = [0] * 10

    for i in temp:
        count[int(i)] += 1

    max_count = 0
    max_value = 0
    for i, val in enumerate(count):
        if max_value <= val:
            max_value = val
            max_count = i
            


    print(f'#{test_case} {max_value} {max_count}')



    # 값을 인덱스로 사용하기 
    # cntlst = [0]*10
    # for i in range(10):
    #     n = int(input())
    #     cntlst[n] += 1 