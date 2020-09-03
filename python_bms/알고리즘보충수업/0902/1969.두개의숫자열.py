def calc(long,short): 
    max_value = -987654321 # 임의의 아주 작은 값 
    for i in range(len(long)-len(short)+1):
        result = 0
        for j in range(len(short)):
            result += long[i+j]*short[j]
        if max_value < result:
            max_value = result
            
    return max_value
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # 두개로 정해져있기때문에 리스트로 굳이 받지 않았다. 

    numsA = list(map(int,input().split()))
    numsB = list(map(int,input().split()))

    if len(numsA) > len(numsB):
        ans = calc(numsA, numsB)
    else:
        ans = calc(numsB, numsA)
    
    print('#{} {}'.format(tc, ans))