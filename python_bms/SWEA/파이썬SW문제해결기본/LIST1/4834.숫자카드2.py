T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = input()
    temp = []
    for card in cards:
        temp.append(card)
    
    count = [0] * 10

    for i in temp:
        count[int(i)] += 1

    max_count = 0
    max_value = 0

    for i, value in enumerate(count):
        if max_value <= value:
            max_value = value
            max_count = i
    
    print('#{} {} {}'.format(tc, max_count, max_value))
        