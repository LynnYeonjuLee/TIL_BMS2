T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int,input().split()))
    lowest = nums[0]
    largest = nums[0]
    for num in nums:
        if num < lowest:
            lowest = num
        elif num > largest:
            largest = num

    print('#{} {}'.format(tc, largest-lowest))


# 처음 이 문제를 풀었을 때 나의 방법 

# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     numbers = list(map(int,input().split()))
#     srt_nums = sorted(numbers)
#     result = srt_nums[len(numbers)-1] - srt_nums[0]
#     print(f'#{test_case} {result}')
