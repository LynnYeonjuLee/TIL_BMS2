A = int(input())
B = int(input())
C = int(input())
number = A * B * C
num = str(number)
for i in range(10): # 9를 입력해서 첨에 틀림 !
    count = 0
    for j in range(len(num)):
        if i == int(num[j]):
            count += 1
        else:
            continue
    print(count)
    