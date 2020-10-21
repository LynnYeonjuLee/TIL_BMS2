# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 그중 가장 많은 글자의 개수를 출력하는 프로그램을 만드시오.
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