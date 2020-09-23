from itertools import combinations

heights = [int(input()) for _ in range(9)]
occation = list(combinations(heights, 7))
for i in occation:
    if sum(i) == 100:
        ans = list(i)
        break
ans.sort()
for i in ans:
    print(i)