arr = list(map(int,input().split()))
N = len(arr)
cnt = 0
for i in range(1<<N): # i 는 부분집합
    # i : 00000 => 11111
    # 10101 [1, 3, 22]
    sumV = 0
    lst = []
    for j in range(N):
        if i & (i << j):
            sumV += arr[j] # 값i 의 j 번째 비트가 1이면
            lst.append(arr[j])
    if sumV == 0:
        cnt += 1
        print(lst)
print(cnt)
    