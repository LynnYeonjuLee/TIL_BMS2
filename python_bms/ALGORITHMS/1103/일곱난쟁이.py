h_list = []
for _ in range(9):
    h = int(input())
    h_list.append(h)
# print(h_list)
result = []
for i in range(8):
    for j in range(i+1,9):
        # for k in range(2):
        if h_list[i] + h_list[j] == sum(h_list) - 100:
            result.append(h_list[i])
            result.append(h_list[j])
# print(result)
for i in range(2):
    if result[i] in h_list:
        h_list.remove(result[i])
# print(h_list)
result_h = sorted(h_list)
for i in range(7):
    print(result_h[i])