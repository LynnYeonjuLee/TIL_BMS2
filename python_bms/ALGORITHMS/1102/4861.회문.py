T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    l_lst = []
    result = []
    result1 = []
    cnt = 0 
    cnt1 = 0
    for _ in range(N):
        letters = list(map(str,input()))
        l_lst.append(letters)
    # for _ in range(N):
    #     result = []
        for i in range((N-1)//2):
            if letters[i] != letters[N-i-1]:
                break
            else:
                cnt += 1
                if cnt == ((N-1)//2):
                    result = letters
    if len(result) != 0:
        for a in range(len(result)):
            print(result[a],end='')
    else: 
        for m in range(M):
            for j in range((M-1)//2):
                if l_lst[j][m] != l_lst[M-j-1][m]:
                    break
                else:
                    cnt1 += 1
                    if cnt1 == ((M-1)//2):
                        for m in range(M):
                            for j in range((M-1)//2):
                                result1.append(l_lst[j][m])
        