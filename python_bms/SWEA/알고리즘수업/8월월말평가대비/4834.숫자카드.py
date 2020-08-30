T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = input() # 입력사이에 공간이 없으니까 split를 안해준다. 
    temp = []
    for num in nums:
        temp.append(num)

    num_cnt_lst = [0]*10

    for i in temp:
        num_cnt_lst[int(i)] += 1
    
    max_cnt = 0
    max_num = 0

    for i, val in enumerate(num_cnt_lst):
        if max_num <= val:
            max_num = val 
            max_cnt = i
            
    print('#{} {} {}'.format(tc, max_cnt, max_num))