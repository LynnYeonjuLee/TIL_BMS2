N = int(input())
num_list = []
for n in range(N):
    num = int(input())
    num_list.append(num)
new_list = sorted(num_list)
for num in new_list:
    print(num)