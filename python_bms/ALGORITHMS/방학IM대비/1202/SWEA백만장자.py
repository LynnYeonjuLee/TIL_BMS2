T = int(input())
for t in range(1, T+1):
    N = int(input())
    pr_list = list(map(int,input().split()))
    for i in range(N-1):
        if pr_list[i+1] < pr_list[i]:
            result = 0
        else: # 증가한다면
            result =

