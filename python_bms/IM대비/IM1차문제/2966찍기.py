N = int(input())
answers = list(map(str,input()))
# 상근이 창영이 현진이의 리스트를 만들어 답을 반복적으로 넣어둔다. 
Adrian = [] # 상근
Bruno = [] # 창영
Goran = [] # 현진
a_cnt = 0
b_cnt = 0
g_cnt = 0

for i in range(33):
    Adrian.append('A')
    Adrian.append('B')
    Adrian.append('C')
Adrian.append('A')
for i in range(25):
    Bruno.append('B')
    Bruno.append('A')
    Bruno.append('B')
    Bruno.append('C')
for i in range(16):
    Goran.append('C')
    Goran.append('C')
    Goran.append('A')
    Goran.append('A')
    Goran.append('B')
    Goran.append('B')
Goran.append('C')
Goran.append('C')
Goran.append('B')
Goran.append('B')

for i in range(len(answers)):
    if answers[i] == Adrian[i]:
        a_cnt += 1
    if answers[i] == Bruno[i]:
        b_cnt += 1
    if answers[i] == Goran[i]:
        g_cnt += 1
result = max(a_cnt, b_cnt, g_cnt)
name_result = []
if a_cnt == result:
    name_result.append('Adrian')
if b_cnt == result:
    name_result.append('Bruno')
if g_cnt == result:
    name_result.append('Goran')
print(result)
for i in range(len(name_result)):
    print(name_result[i])


# 나머지 연산을 활용해서 간단하게 만들어보자!!
