N = int(input())
d_list = []
for _ in range(N):
    dice = list(map(int,input().split())) # A, B, C, D, E, F
    d_list.append(dice)
# print(d_list)
bottom = 0
top = 0
cnt = 0


for j in range(N):
    one_six = [1, 2, 3, 4, 5, 6]
    for i in range(6):
        bottom = d_list[j][i]
        print(bottom)
        if i == 0:
            top = d_list[j][5]
            one_six.remove(bottom)
            one_six.remove(top)
            max_side = max(one_six)
            cnt += max_side
            bottom = top
        elif i == 1:
            top = d_list[j][3]
            one_six.remove(bottom)
            one_six.remove(top)
            max_side = max(one_six)
            cnt += max_side
            bottom = top
        elif i == 2:
            top = d_list[j][4]
            one_six.remove(bottom)
            one_six.remove(top)
            max_side = max(one_six)
            cnt += max_side
            bottom = top
        elif i == 3:
            top = d_list[j][1]
            one_six.remove(bottom)
            one_six.remove(top)
            max_side = max(one_six)
            cnt += max_side
            bottom = top
        elif i == 4:
            top = d_list[j][2]
            one_six.remove(bottom)
            one_six.remove(top)
            max_side = max(one_six)
            cnt += max_side
            bottom = top
        else:
            top = d_list[j][0]
            one_six.remove(bottom)
            one_six.remove(top)
            max_side = max(one_six)
            cnt += max_side
            bottom = top
        print(top)


        #
        #     # print(bottom)
        #     # top = d_list[j][5]
        #     one_six.remove(bottom)
        #     # one_six.remove(top)
        #     max_side = max(one_six)
        #     cnt += max_side
        # elif bottom == 2:
        #     # top = d_list[j][3]
        #     one_six.remove(bottom)
        #     # one_six.remove(top)
        #     max_side = max(one_six)
        #     cnt += max_side
        # elif bottom == 3:
        #     # top = d_list[j][4]
        #     one_six.remove(bottom)
        #     # one_six.remove(top)
        #     max_side = max(one_six)
        #     cnt += max_side
        # elif bottom == 4:
        #     # top = d_list[j][1]
        #     one_six.remove(bottom)
        #     # one_six.remove(top)
        #     max_side = max(one_six)
        #     cnt += max_side
        # elif bottom == 5:
        #     top = d_list[j][2]
        #     one_six.remove(bottom)
        #     # one_six.remove(top)
        #     max_side = max(one_six)
        #     cnt += max_side
        # else:
        #     top = d_list[j][0]
        #     one_six.remove(bottom)
        #     # one_six.remove(top)
        #     max_side = max(one_six)
        #     cnt += max_side
print(cnt)