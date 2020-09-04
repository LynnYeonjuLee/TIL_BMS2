for tc in range(1,int(input())+1):
    N,M = map(int,input().split()) 
    arr = [list(input()) for _ in range(N)]
    min1 = N*M
    cnt1 = 0
    for w in range(0,N-2): # 화이트
        for k in range(0,M):
            if arr[w][k] != 'W':
                cnt1 += 1
 
        cnt2 = 0
        for b in range(w+1,N-1): # 블루
            for k in range(0,M):
                if arr[b][k] != 'B':
                    cnt2 += 1
 
            cnt3 = 0
            for r in range(b+1,N): # 레드
                for k in range(0,M):
                    if arr[r][k] != 'R':
                        cnt3 += 1
          
            cnt = cnt1 + cnt2 + cnt3
            if min1 > cnt:
                min1 = cnt
    print(f'#{tc} {min1}')