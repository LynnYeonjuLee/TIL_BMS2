T = int(input())
for tc in range(1, T+1):
    words = [0]*5
    maxlen = 0
    for i in range(5):
        words[i] = list(input())
        if len(words[i]) > maxlen:
            maxlen = len(words[i])
    print('#{}'.format(tc), end=' ')
    for i in range(maxlen):
        for j in range(5):
            if len(words[j]) > i:
                print(words[j][i], end= ' ')
    print()