T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int,(input().split())))
    card1 = len(cards) // N * 2
    for i in range(len(cards)):
        for j in range(len(cards)):
            a = cards[:(i+j)//2+1]
            b = cards[(i+j)//2+1:]

# 낼 다시풀게 머리 멈춤 