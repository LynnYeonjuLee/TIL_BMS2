T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    start = 0
    check_nums = [] # 곱의 결과들
    for i in range(N):
        for j in range(i+1, N):
            check_nums.append(nums[i]*nums[j])
    print(check_nums)
    isIncreasing = False
    inc_num_list = []
    num_length = 0
    # temp_check_num = []
    first_num = 0
    second_num = 0
    check_nums_temp = 0
    result = 0
    # if N == 1:
    #     result = -1
    # else:
    for i in range(len(check_nums)):
        num_length = len(str(check_nums[i]))
        # print(num_length)
        check_nums_temp = check_nums[i]
        temp_check_num = []
        if num_length == 1:
            isIncreasing = False
            result = -1
        else:
            while num_length >= 1:
                first_num = check_nums_temp // (10**(num_length-1))
                # print(check_nums_temp)
                # print(first_num)
                second_num = check_nums_temp % (10**(num_length-1))
                check_nums_temp = second_num
                temp_check_num.append(first_num)
                if second_num < 10:
                    temp_check_num.append(second_num)
                    break
                num_length -= 1
            # print(temp_check_num)
            # print(check_nums[i])
        for a in range(len(temp_check_num)-1):
            if temp_check_num[a] <= temp_check_num[a+1]:
                isIncreasing = True
            else:
                isIncreasing = False
                break
        if isIncreasing == True:
            # print(check_nums[i])
            inc_num_list.append(check_nums[i])
    # print(inc_num_list)
    if len(inc_num_list) == 0:
        result = -1
    else:
        result =  max(inc_num_list)
        # print(inc_num_list)

    print('#{} {}'.format(t,result))