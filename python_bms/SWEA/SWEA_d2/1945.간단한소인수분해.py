T = int(input())
for test_case in range(1, T+1):
    numbers = [2, 3, 5, 7, 11]
    N = int(input())
    result = []
    
    for number in numbers:
        count = 0
        while N % number == 0:
            N = N // number
            count += 1
        result.append(count)
        
    print('#{} {}'.format(test_case, ' '.join(map(str,result)))) # join 주의하자 