def findPage (p):
    cnt = 0
    l = 1
    r = P

    while True:
        c = int((l+r)/2)
        cnt += 1
        if p > c:
            l = c
        elif p == c:
            break
        else:
            r = c
    return cnt

T = int(input())

for tc in range(1, T+1):
    P, pa, pb = list(map(int, input().split())) # P : 전체쪽수, pa: A가 찾을 쪽 번호 pb: B 가 찾을 쪽 번호
    cnt_a = 0
    cnt_b = 0
    result = ''
    cnt_a = findPage(pa)
    cnt_b = findPage(pb)

    if cnt_a > cnt_b:
        result = 'B'
    elif cnt_a == cnt_b:
        result = 0
    else: 
        result = 'A'




    print(f'#{tc} {result}')



    # 원래 있던 알고리즘에 못찾은 경우 카운트 증가 
    # 찾으면 return cnt
