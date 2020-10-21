T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    num = input()
    month31 = ['01', '03', '05', '07', '08', '10', '12']
    month30 = ['04', '06', '09', '11']
    year = num[0:4]
    month = num[4:6]
    day = num[6:8]
    result = 0
    yes_cal =  f'#{test_case} {year}/{month}/{day}'
    if month in month31:
        if int(day)>31:
            print(f'#{test_case} -1')
            continue
        else:
            print(yes_cal)
    elif month in month30:
        if int(day)>30:
            print(f'#{test_case} -1')
            continue
        else:
            print(yes_cal)
    elif month == '00':
        print(f'#{test_case} -1')
        continue
    else:
        if int(day)>28:
            print(f'#{test_case} -1')
            continue
        else:
            print(yes_cal)