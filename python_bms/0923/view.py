import sys
sys.stdin = open("view_input.txt")
T = 10
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split() ))
    ans = 0

    for i in range(2, N-2):
        minV = 987654321
        for j in range(5):
            if j != 2:
                if arr[i] - arr[i-2+j] < minV:
                    minV = arr[i] - arr[i-2+j]
        if minV > 0 :
            ans += minV
    print("#{} {}".format(tc+1, ans))