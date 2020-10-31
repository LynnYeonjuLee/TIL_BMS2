T = int(input())
for t in range(1, T+1):
    N, M = map(int,input().split())
    l_lst = []
    result = []
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
                if cnt = N:
                    result = letters
    print(result)