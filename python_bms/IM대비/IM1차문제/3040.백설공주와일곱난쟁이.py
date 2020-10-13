d_l = []
for i in range(9):
    d_l.append(int(input()))

# dwarf1 = int(input())
# dwarf2 = int(input())
# dwarf3 = int(input())
# dwarf4 = int(input())
# dwarf5 = int(input())
# dwarf6 = int(input())
# dwarf7 = int(input())
# dwarf8 = int(input())
# dwarf9 = int(input())
# d_l = []
# d_l.append(dwarf1)
# d_l.append(dwarf2)
# d_l.append(dwarf3)
# d_l.append(dwarf4)
# d_l.append(dwarf5)
# d_l.append(dwarf6)
# d_l.append(dwarf7)
# d_l.append(dwarf8)
# d_l.append(dwarf9)

sum_all = sum(d_l)

# sum_all - 두가지의 합 = 100 이 되면 된다. 
for i in d_l:
    for j in d_l:
        if i != j:
            if sum_all - i - j == 100:
                d_l.remove(i)
                # print(d_l)   
                d_l.remove(j)
                # print(d_l)
                # break
for i in range(len(d_l)):
    print(d_l[i])
  