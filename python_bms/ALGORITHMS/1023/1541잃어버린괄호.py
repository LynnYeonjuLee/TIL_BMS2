question = input().split('-')
# print(question)
l = []
for i in question:
    cnt = 0
    add = i.split('+')
    for j in add:
        cnt += int(j)
    l.append(cnt)
n = l[0]
for i in range(1, len(l)):
    n -= l[i]
print(n)
    