import sys
sys.stdin = open("flatten_input.txt")

T = 10
for tc in range(1, 11):
    dumps = int(input())
    dumps_arr = list(map(int,input().split()))
    # temp = []
    # for i in range(len(dumps_arr)):
    #     temp.append(dumps_arr[i])
    #
    for i in range(dumps):
        max_idx = 0
        min_idx = 0
        for j in range(1, 100):
            if dumps_arr[max_idx] < dumps_arr[j]:
                max_idx = j
            if dumps_arr[min_idx] > dumps_arr[j]:
                min_idx = j
        dumps_arr[max_idx] -= 1
        dumps_arr[min_idx] += 1
    # 최대값 최소값을 구해서 빼야한다.
    result = max(dumps_arr)-min(dumps_arr)
    # result = dumps_arr[max_idx]-dumps_arr[min_idx]
    print('#{} {}'.format(tc, result))
