T = int(input())
for t in range(1, T+1):
    N, S = input().split()
    arr = []
    for _ in range(N):
        g_l = list(map(int,input().split()))
        arr.append(g_l)
    print(arr)

    