heights = []
for i in range(9):
    heights.append(int(input()))
sum1 = sum(heights)

finish = False
for i in range(8):
    for j in range(i+1, 9):
        if heights[i]+heights[j] == sum1 - 100:
            save = [i, j]
            finish = True
            break
    if finish:
        break
del heights[save[0]]
del heights[save[1]-1]

heights.sort()

for i in heights:
    print(i)