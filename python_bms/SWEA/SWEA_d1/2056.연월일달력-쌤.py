days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T - int(input())
for tc in range(1, T+1):
    temp = input()

    year = temp[:4]
    month = temp[4:6]
    day = temp[6:]

    flag = True # 유효한지 아닌지를 체크하는 

    if int(month) <= 0 or int(month) > 13:
        flag = False
    
    elif int(day) > days[int(month)] or int(day) <= 0:
        flag = False


    if flag: 
        print('#{} {}/{}/{}'.format(tc, year, month, day))
    else:
        print('#{} -1'.format(tc))