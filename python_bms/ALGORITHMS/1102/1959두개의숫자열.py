T = int(input())
for t in range(1, 1+T):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    # temp = []
    compare = []
    result = 0
    if len(B) > len(A):
        for i in range(len(B)-len(A)+1):
            # start = i
            new_sum = 0
            for j in range(len(A)):
                new_sum += A[j]*B[i+j] 
            compare.append(new_sum)
        result = max(compare)
        # print(compare)

    else:
        for i in range(len(A)-len(B)+1):
            # start = i
            new_sum = 0
            for j in range(len(B)):
                new_sum += B[j]*A[i+j] 
            compare.append(new_sum)
        result = max(compare)
        # print(compare)
    # for i in range(abs(len(B)-len(A))+1):
    #     if len(B) > len(A):
            
    #     else:
    print('#{} {}'.format(t,result))
