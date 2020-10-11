N = int(input())
count = 0
next = 0 
check = N 
next1 = 0
# 다음 숫자가 받아온 숫자와 같아질 때까지 
while True:
    next1 = N//10 + N % 10 
    next = 10*(N%10) + next1%10
    count += 1
    N = next
    if next == check:
        break
print(count)
