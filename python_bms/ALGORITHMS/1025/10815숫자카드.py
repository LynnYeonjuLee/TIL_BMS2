# 시간초과
N = int(input())
cards = set(map(int,input().split()))
M = int(input())
checks = list(map(int,input().split()))
result = []
for check in checks:
    if check in cards:
        print(1,end=' ')
    else: 
        print(0,end=' ')
# dict 나 이분탐색으로 풀면 된다. 

# N = int(input())
# cards = list(map(int,input().split()))
# cards = sorted(cards)
# M = int(input())
# checks = list(map(int,input().split()))
# for i in range(M):
    