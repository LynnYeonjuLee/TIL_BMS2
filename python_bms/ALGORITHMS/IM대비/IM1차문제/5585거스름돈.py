mon = int(input())
target = 1000 - mon
coin_500 = target // 500
coin_100 = (target % 500) // 100
coin_50 = (target % 500) % 100 //50
coin_10 = (target % 500) % 100 % 50 // 10
coin_5 = (target % 500) % 100 % 50 % 10 // 5
coin_1 = (target % 500) % 100 % 50 % 10 % 5 // 1
print(coin_500+coin_100+coin_50+coin_10+coin_5+coin_1)
