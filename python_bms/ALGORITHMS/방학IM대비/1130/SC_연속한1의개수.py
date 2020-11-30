T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int,input()))
    cnt = 0
    cnt_list = []
    for i in range(nums):
        if nums[i] == 0:
            cnt_list.append(cnt)
            cnt = 0

        else:
            cnt += 1
    result = max(cnt_list)

    print('#{} {}.format(t, result)')

