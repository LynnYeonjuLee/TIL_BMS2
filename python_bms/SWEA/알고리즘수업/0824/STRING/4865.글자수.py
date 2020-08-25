TC = int(input())

for tc in range(1, TC+1):
    str1 = input()
    str2 = input()
    cnt1, cnt2 = 0, 0

    for i in str1:
        for j in str2:
            if i == j:
                cnt1 += 1
        if cnt1 > cnt2:
            cnt2 = cnt1
        cnt1 = 0
    print("#%d %d"%(tc, cnt2)) 