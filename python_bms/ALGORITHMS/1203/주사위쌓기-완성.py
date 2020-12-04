N = int(input())
dices = [list(map(int,input().split())) for _ in range(N)]
temp = []

for i in range(N):
    dice = []
    for j in range(6):
        if j == 0:
            dice.append([dices[i][j], dices[i][5]])
        elif j == 1:
            dice.append([dices[i][j], dices[i][3]])
        elif j == 2:
            dice.append([dices[i][j], dices[i][4]])
        elif j == 3:
            dice.append([dices[i][j], dices[i][1]])
        elif j == 4:
            dice.append([dices[i][j], dices[i][2]])
        elif j == 5:
            dice.append([dices[i][j], dices[i][0]])
    dice.sort()
    temp.append(dice)
print(temp)
result = []
for i in range(6):
    num_sum = 0
    bottom = temp[0][i][0]
    top = temp[0][i][1]
    for j in range(N):
        for k in range(6):
            if temp[j][k][0] == bottom:
                top = temp[j][k][1]
        if (bottom + top) == 11:
            num_sum += 4
        elif bottom == 6 or top == 6:
            num_sum += 5
        else:
            num_sum += 6
        bottom = top
    result.append(num_sum)

print(max(result))
