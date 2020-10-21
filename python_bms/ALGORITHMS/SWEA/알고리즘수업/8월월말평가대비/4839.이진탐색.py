# def binarySearch(a, low, high, key):
#     if low > high:
#         return False 
#     else: 
#         middle = (low + high) // 2
#         if key == a[middle]:
#             return True
#         elif key < a[middle]:
#             return binarySearch(a, low, middle-1, key)
#         elif a[middle] < key:
#             return binarySearch(a, middle+1, high, key)



T = int(input())

for tc in range(1, T+1):
    P, pa, pb = list(map(int, input().split())) # P : 전체쪽수, pa: A가 찾을 쪽 번호 pb: B 가 찾을 쪽 번호
    cnt_a = 0
    cnt_b = 0
    result = ''
    l1 = 1
    r1 = P
    l2 = 1
    r2 = P
    c1 = 0
    c2 = 0
    while pa != c1:
        c1 = int((l1+r1)/2)
        cnt_a += 1
        if pa > c1:
            l1 = c1
        elif pa == c1:
            break
        else:
            r1 = c1
    while pb != c1:
        c2 = int((l2+r2)/2)
        cnt_b += 1
        if pb > c2:
            l2 = c2
        elif pb == c2:
            break
        else:
            r2 = c2

    if cnt_a > cnt_b:
        result = 'B'
    elif cnt_a == cnt_b:
        result = 0
    else: 
        result = 'A'




    print(f'#{tc} {result}')