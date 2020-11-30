T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int,input()))
    cnt = 0
    # print(nums)
    cnt_list = []
    for num in nums:
        if num == 0:
            cnt_list.append(cnt)
            cnt = 0
        else:
            cnt += 1
            cnt_list.append(cnt)
    result = max(cnt_list)
    # print(cnt_list)
    print('#{} {}'.format(t, result))

