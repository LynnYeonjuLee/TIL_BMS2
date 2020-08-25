score_list = []
score_sum = 0
for i in range(5):
    score = int(input())
    if score > 40:
        score_sum += score
    else:
        score_sum += 40
print(f'{int(score_sum/5)}')
