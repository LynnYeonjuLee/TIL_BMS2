a = [4, 1, 2, 3]
b = sorted(a)
print(b)

a.sort(reverse=True)
print(a)

c1 = [[1, 2], [2, 3], [4, 1]]
c1.sort()
print(c1)

c2 = [[1, 2], [2, 3], [4, 1]]
c2.sort(key=lambda x: x[1])
print(c2)