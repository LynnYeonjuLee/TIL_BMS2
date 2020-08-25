number = int(input())
for i in range(1, number+1): # 각 층을 출력 
    # i: 1, 2, 3, 4
    for j in range(1, i+1): # j:1
        print(j, end=" ")
    print()
