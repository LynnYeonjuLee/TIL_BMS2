T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    result_lst = []
    if len(A) < len(B):
        for i in range(len(B)-len(A)+1):
            sum_ = 0
            for j in range(len(A)):
                sum_ += (A[i]*B[i+j])
            result_lst.append(sum_)
        result = max(result_lst)
    else:
        for i in range(len(A)-len(B)+1):
            sum_ = 0
            for j in range(len(B)):
                sum_ += (B[i]*B[i+j])
            result_lst.append(sum_)
        result = max(result_lst)