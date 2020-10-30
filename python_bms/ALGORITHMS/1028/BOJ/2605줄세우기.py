N = int(input())
orders = list(map(int,input().split()))
# 첫번째 사람은 무조건 0번 
result = []
result.append(orders[0])
for i in range(1, len(orders)):
    if 