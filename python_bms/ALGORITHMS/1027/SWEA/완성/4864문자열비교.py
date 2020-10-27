T = int(input())
for t in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    if str1 in str2:
        print('#{} {}'.format(t, 1))
    else:
        print('#{} {}'.format(t, 0))
