num_list = []
for i in range(9):
    number = int(input())
    num_list.append(number)
max_num = 0
for i in range(9):
    if num_list[i] > max_num:
        max_num = num_list[i]
        location = i+1
print(max_num)
print(location)
