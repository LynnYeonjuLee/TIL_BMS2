price_list = []
burger_list = []
drink_list = []
for i in range(0, 5):
    price = int(input())
    price_list.append(price)
for i in range(0, 3):
    burger_list.append(price_list[i])
burger_list2 = sorted(burger_list)
for i in range(3, 5):
    drink_list.append(price_list[i])
drink_list2 = sorted(drink_list)

print(burger_list2[0]+drink_list2[0]-50)