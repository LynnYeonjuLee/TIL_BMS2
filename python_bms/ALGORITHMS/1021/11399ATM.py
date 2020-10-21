T = int(input())
mins = list(map(int,input().split()))
cnt = 0
result_list = []
new_mins = sorted(mins)
for i in new_mins:
    cnt += i
    result_list.append(cnt)
print(sum(result_list))