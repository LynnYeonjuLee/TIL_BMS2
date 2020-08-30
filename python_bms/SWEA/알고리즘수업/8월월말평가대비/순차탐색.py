# 정렬이 안되어있는 경우
def seq_search(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i += 1
    if i < n: # 이부분 !!
        return i
    else:
        return -1

arr = [4, 9, 11, 23, 2, 19, 7]
key = 23
print(seq_search(arr, len(arr), key))

# 정렬이 되어있는 경우
def seq_search(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i += 1
    if i < n and a[i] == key: # 이부분 !!
        return i
    else:
        return -1

arr = [1, 2, 3, 4, 5, 6, 17, 18, 19] # 17을 만나면 빠져나온다.
key = 12
print(seq_search(arr, len(arr), key))