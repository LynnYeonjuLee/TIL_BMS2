#  문자의 길이가 길어지면....메모리 초과........

from itertools import permutations
l = list(map(str,input())) # AABB
# l_r = l[::-1] 
# print(l_r) # BBAA
# 조합할 수 있는 경우의 수를 다 찾아주고 
new_l = list(permutations(l,len(l)))
# 팰린드롬을 만족하는 경우가 있다면 출력하고 
result = []
pal = False
for i in range(len(new_l)):
    cnt = 0
    for j in range(len(l)//2):
        if new_l[i][j] == new_l[i][-j-1]:
            cnt += 1
        else:
            pass
    if cnt == len(l)//2:
        pal = True
        result = new_l[i]
if pal == True:
    for i in range(len(result)):
        print(result[i],end='')
else: # 없다면 "I'm Sorry Hansoo" 를 출력한다. 
    print("I'm Sorry Hansoo")



