T = int(input())
scores = list(map(int,input().split()))
M = max(scores)
new_score_list = []
for i in range(len(scores)):
    new_score = scores[i] / M * 100
    new_score_list.append(new_score)
print(round(sum(new_score_list)/len(new_score_list),6))
