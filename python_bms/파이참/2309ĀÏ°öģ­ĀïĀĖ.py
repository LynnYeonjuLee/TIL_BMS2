def find(s, a, n):
    global check
    if check:
        return
    if a == 7:
        if sum(ans) == 100:
            check = True
        return
    if s == 9:
        return
    ans[a] = arr1[s]
    find(s+1, a+1, n) # 선택을 한 경우
    find(s+1, a, n) # 선택을 안 한 경우

check = False
arr1 = []
for i in range(9):
    height = int(input())
    arr1.append(height)
ans = [[0] for _ in range(7)] # 선택할 난쟁이가 들어가 있는 배열
find(0, 0, arr1)
ans.sort()
for x in range(7):
    print('{}'.format(ans[x]))