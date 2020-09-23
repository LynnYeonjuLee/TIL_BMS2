N = int(input())
card = list(map(int, input().split()))
line = []
for i in range(len(card)):
    line.insert(card[i], i+1) ##  이부분 궁금
line = line[::-1]
print(*line)