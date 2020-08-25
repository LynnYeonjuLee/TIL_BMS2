T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    meters = list(map(int,input().split()))
    count = 0

    for i in range(len(meters)):
        distance = abs(0 - abs(meters[i]))
        for j in range(1, len(meters)):
            new_distance = abs(0 - abs(meters[j]))
            if distance > new_distance:
                distance = new_distance
            # to_zero.append(distance)
        if distance == abs(meters[i]):
            count+= 1
    print('#{} {} {}'.format(test_case, distance, count))


