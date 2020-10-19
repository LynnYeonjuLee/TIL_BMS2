N = list(map(int,input()))
num_set = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for i in N:
    if i == 6 or i == 9:
        num_set[6] += 0.500001
    else: 
        num_set[i] += 1

com = 0.0
for i in range(len(num_set)):
    if com < num_set[i]:
        com = num_set[i]
    else:
        pass

print(round(com))
