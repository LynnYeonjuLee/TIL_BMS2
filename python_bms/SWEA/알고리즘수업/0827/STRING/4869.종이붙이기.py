
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    result = list()
    result.append(1)
    result.append(3)
    for i in range(2,N//10):
        num = result[i-1] + result[i-2] * 2
        result.append(num)

    print("#{} {}" .format(tc, result[i]))