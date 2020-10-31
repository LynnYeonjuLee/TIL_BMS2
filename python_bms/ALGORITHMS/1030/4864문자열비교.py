T = int(input())
for t in range(1, T+1):
    str1 = str(input())
    str2 = str(input())
    if str1 in str2:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(t, result))