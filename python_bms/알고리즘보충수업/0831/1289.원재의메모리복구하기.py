T = int(input())
for tc in range(1, T+1):
    bit_nums = list(input())
    for bit_num in bit_nums:
        initial = [0] * len(bit_nums)
        cnt = 0 
        while initial != bit_nums:
            for i in range(len(bit_nums)):
                initial << i
                cnt += 1
    print('#{} {}'.format(tc, cnt))