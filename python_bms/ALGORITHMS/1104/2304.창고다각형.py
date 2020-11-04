N = int(input())
arr = [0] * 1000
for _ in range(N):
    L, H = map(int,input().split())
    arr[L] = H
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:

# print(arr)