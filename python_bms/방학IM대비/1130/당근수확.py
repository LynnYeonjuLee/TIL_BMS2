T = int(input())
for t in range(1, T+1):
    N = int(input())
    carrots = list(map(int,input().split()))
    worker1 = 0
    # worker2 = 0
    standard = 0
    sum_carrots = sum(carrots) # 총 당근 개수
    # print(sum_carrots)
    m_list1 = []
    # m_list2 = []
    while standard < N:
        for i in range(standard):
            worker1 += carrots[i]
        m_list1.append(worker1)
        # for i in range(standard+1, N):
        #     worker2 += carrots[i]
        # m_list2.append(worker2)
        standard += 1
    # print(m_list1)
    # print(m_list2)
    result_list1 = []
    # result_list2 = []
    for i in range(len(m_list1)-1):
        result_list1.append(m_list1[i+1]-m_list1[i])
    result_list1.append(carrots[1]+result_list1[N-2])
    # for i in range(len(m_list2)-1):
    #     result_list2.append(m_list2[i+1]-m_list2[i])
    # print(result_list1)
    # print(result_list2)
    final_list = []
    for i in range(len(result_list1)):
        final_list.append(sum_carrots-result_list1[i])
    # print(final_list)
    min_diff = sum_carrots
    for i in range(len(final_list)):
        if final_list[i] >= 0:
            if abs(final_list[i]-result_list1[i]) < min_diff:
                min_diff = abs(final_list[i]-result_list1[i])
                result_idx = i+1
    # print(result_idx)
    # print(min_diff)
    print('#{} {} {}'.format(t, result_idx, min_diff))







