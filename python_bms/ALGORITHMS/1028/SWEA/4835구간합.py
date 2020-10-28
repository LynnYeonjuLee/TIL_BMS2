T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    nums = list(map(int,input().split()))
    sum_list = []

    for i in range(0,N-M+1):
        sum1 = 0
        for j in range(i,i+M):
            sum1 += nums[j]
        sum_list.append(sum1)
    print('#{} {}'.format(t, max(sum_list)-min(sum_list)))
    '''
    2
    10 3
    1 2 3 4 5 6 7 8 9 10
    10 5
    6262 6004 1801 7660 7919 1280 525 9798 5134 1821
    '''
