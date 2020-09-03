T = int(input())
for test_case in range(1, T+1):
    A, B = list(map(int,input().split()))
    N = len(A)
    M = len(B)
    move = N - M 
    sum_ab = 0
    sum_lst = []
    if move > 0:
        for i in range(N-M+1):
            for j in range(M):
                sum_ab += A[i] * B[j]
                sum_lst.append(sum_ab)
    elif move == 0:
        for i in range(N):
            sum_ab += A[i] * B[i]
            sum_lst.append(sum_ab)
    sorted_lst = sorted(sum_lst)
    result = sorted_lst[-1]



    print('#{} {}'.format(test_case, result))