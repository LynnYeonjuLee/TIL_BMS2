A, B, V = list(map(int,input().split()))
snail = 0
day = 0
while snail < V:
    snail += A
    if snail > V:
        day -= 1
    else:
        snail -= B
    day += 1
print(day)
