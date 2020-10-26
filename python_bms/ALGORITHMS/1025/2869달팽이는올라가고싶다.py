# 시간초과남
A, B, V = map(int,input().split())
snail = 0
if (V-B) % (A-B) != 0:
    snail = ((V-B)//(A-B)) + 1
else:
    snail = ((V-B)//(A-B))
print(snail)
