num1, num2 = map(int,input().split())
cnt = 1
while num1 != num2:
    cnt += 1
    num2 += 1
print(cnt)