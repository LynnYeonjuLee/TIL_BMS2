for _ in range(4):
    a, b, c, d, A, B, C, D = map(int, input().split())
    # d
    if c < A or D < b or d < B or C < a:
        result = 'd'
    # c
    elif (b == D or B == d) and (a == C or c == A):
        result = 'c'
    # b
    elif b == D or B == d or a == C or c == A:
        result = 'b'
    # a
    else:
        result = 'a'
    print('{}'.format(result))