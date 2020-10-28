sen = input()
sen = sen.strip()
if len(sen) == 0:
    print(0)
else:
    cnt = 1
     # 공백을 다 없애준다. 
    for i in range(len(sen)):
        if sen[i] == ' ':
            cnt += 1
    print(cnt)
    
# print(len(input().split())) # 갓준호는 한 줄로 풀었다..