h_l = []
for _ in range(9):
    h = int(input())
    h_l.append(h)
height = sum(h_l)
d1 = 0
d2 = 0
for i in range(8):
    for j in range(i+1, 9):
        if height - h_l[i] - h_l[j] == 100:
            d1 = h_l[i]
            d2 = h_l[j]
h_l.remove(d1)
h_l.remove(d2)
s_h_l = sorted(h_l)
for i in s_h_l:
    print(i)


