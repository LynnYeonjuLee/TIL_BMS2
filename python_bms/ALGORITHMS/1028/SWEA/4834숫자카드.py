T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(int,input()))
    arr = [0] * 10
    for card in cards:
        arr[card] += 1
    max_std = 0
    max_idx = 0
    # print(arr)
    for i in range(len(arr)):
        if arr[i] > max_std:
            max_std = arr[i] 
            max_idx = i
        elif arr[i] == max_std: 
            max_idx = i
    print('#{} {} {}'.format(t, max_idx, max_std))
