while True:
    nums = list(map(int,input().split()))
    if len(nums) == 1 and 0 in nums:
        break
    else:
        a = []
        b = []
        nums.pop(0)
        new_nums = sorted(nums)


        # 0 을 일단 다 지워준다.
        z_cnt = new_nums.count(0)
        for _ in range(z_cnt):
            new_nums.remove(0)


        a.append(new_nums[0])
        new_nums.pop(0)
        # print(new_nums)
        b.append(new_nums[0])
        new_nums.pop(0)
        # print(new_nums)
        for i in range(z_cnt):
            new_nums.append(0)
        new_nums2 = sorted(new_nums)
        while len(new_nums2) != 0 :
            a.append(new_nums2[0])
            new_nums2.pop(0)
            if len(new_nums2) != 0:
                b.append(new_nums2[0])
                new_nums2.pop(0)
        a = int(''.join(map(str,a)))
        b = int(''.join(map(str,b)))
        # print(new_nums2)

        print(a+b)
