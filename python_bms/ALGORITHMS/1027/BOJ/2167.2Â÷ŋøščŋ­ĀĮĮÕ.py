# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.
N, M = map(int,input().split())
nums_list = []
for _ in range(N):
    nums = list(map(int,input().split()))
    nums_list.append(nums)
K = int(input())
for _ in range(K):
    i, j, x, y = list(map(int,input().split()))
    sum = 0
    
    for a in range(j-1,y):
        for b in range(i-1,x):    
            sum += nums_list[b][a]
    print(sum)