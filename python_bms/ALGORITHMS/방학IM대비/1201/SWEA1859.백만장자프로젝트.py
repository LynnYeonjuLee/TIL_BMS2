# 하루 최대 1 구매 가능 , 판매는 얼마든지 가능
T = int(input())
for t in range(1, T+1):
    N = int(input())
    price_list = list(map(int,input().split()))
    max_price = price_list[0]
    result = 0
    result_list = []
    buying = []
    buying.append(max_price)
    for i in range(1, len(price_list)):
        if price_list[i] >= max_price:
            max_price = price_list[i]
            # 그 전 날들의 물건 개수 * 현재의 max 가격 - 그전 날들의 물건값  result
            buying.append(price_list[i])
            result = max_price * len(buying) - sum(buying)
            # 리스트에 담아준다.
            result_list.append(result)
            result = max(result_list)

        else:
            # 만약 max_price 보다 큰 것이 없다면
            max_price = price_list[i]
            buying.clear()
            buying.append(price_list[i])
            result = max_price * len(buying) - sum(buying)
            # buying.pop(-1)
            # 리스트에 담아준다.
            result_list.append(result)
            result = max(result_list)
        if result < 0:
            result = 0

    print(result)

