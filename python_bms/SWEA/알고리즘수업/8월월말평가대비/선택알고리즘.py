def selection(a, k):
    # i : 0 ~ len(n) - 1
    for i in range(k): # 0, 1, 2, 3
        # 최소값찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a[k-1]

arr = [64, 25, 10, 22, 11]


print(selection(arr, 3))  # 세번째 큰 값