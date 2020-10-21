l = list(map(str,input()))
# l2 = l
l_yes = []
l_no = []
print(l)
for i in range(len(l)):  
    if l.count(l[i]) % 2 == 0:
        for j in range(l.count(l[i])//2):
            l_yes.append(l[i])
            l.remove(l[i])
    else:
        l_no.append(l[i])
# if len()
print(l_yes)
print(l_no)
print(l2)
