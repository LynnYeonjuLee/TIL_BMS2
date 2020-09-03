T = int(input())
for tc in range(1, T+1): 
    N = input() # 이게 헷갈렸다 
    scores = list(map(int,input().split()))
    cnt = [0]*101 # 0점부터 100점까지이므로 
    for i in scores:
        cnt[i] += 1
    max_score = 0
    result_max = 0
    for i in range(1, len(cnt)): # range(101)
        if max_score <= cnt[i]:
            max_score = cnt[i]
            result_max = i
    
    print('#{} {}'.format(tc, result_max))


