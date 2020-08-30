#다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.

# 다음과 같은 5X5 배열에서 최댓값은 29이다.
#  내부함수 sum 쓰지 않는다. 
for test_case in range(1, 11):
    n = int(input())
    arr_list = []
    for num in range(100): # 2차원배열생성 
        nums = list(map(int,input().split()))
        arr_list.append(nums)
    
    arr_list2 = []
    for i in range(100): #행에 대하여 각 행의 합을 더하고 큰 것을 찾아간다. 
        arr_sum1 = 0
        for j in range(100):
            arr_sum1 += arr_list[j][i]
        arr_list2.append(arr_sum1)

    for j in range(100): 
        arr_sum2 = 0
        for i in range(100):
            arr_sum2 += arr_list[j][i]
        arr_list2.append(arr_sum2)

    arr_sum3 = 0      
    for j in range(100): 
        for i in range(100):
            if i == j:
                arr_sum3 += arr_list[i][i]
    arr_list2.append(arr_sum3)
    arr_sum4 = 0
    for j in range(100):
        for i in range(100):
            if j == 100 - i:
                arr_sum4 += arr_list[j][j]
    arr_list2.append(arr_sum4)
    new_arr_list = sorted(arr_list2)


    print('#{} {}'.format(test_case, new_arr_list[-1]))