d_list = []
for _ in range(9):
    dwarf = int(input())
    d_list.append(dwarf)
# print(d_list)
sum_dwarf = sum(d_list)
# print(sum_dwarf)
e_list = []
for i in range(8):
    for j in range(i+1, 9):
        if sum_dwarf -(d_list[i] + d_list[j]) == 100:
            e_list.append(d_list[i])
            e_list.append(d_list[j])
# print(e_list)
for i in range(2):
    # print(e_list[i])
    if e_list[i] in d_list:
        d_list.remove(e_list[i])
result = sorted(d_list)
for i in range(7):
    print(result[i])