for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    temp = input().split()
    pizza = [(i+1, int(temp[i])) for i in range(M)]
    pizzas = pizza[:N]
    pizza = pizza[N:]
    while len(pizzas) != 1:
        num, cheese = pizzas.pop(0)
        cheese //=2
        if cheese: pizzas.append((num, cheese))
        else : 
            if pizza : pizzas.append(pizza.pop(0))
    print('#{} {}'.format(tc, pizzas.pop()[0]))