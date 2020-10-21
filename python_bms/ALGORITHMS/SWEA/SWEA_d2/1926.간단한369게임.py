N = int(input())
N_list = []
for i in range(1, N+1):
    N_list.append(i)
for num in N_list:
    if num % 3 == 0:
        num = '-'
        while int(num) > 10:
            num = (num // 3) % 3
            num = '--'
        continue
    else: 
        num = num
print(N_list)