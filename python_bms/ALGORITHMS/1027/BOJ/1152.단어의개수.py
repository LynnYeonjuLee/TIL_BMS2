sen = list(map(str,input()))
cnt = 1
for i in range(1, len(sen)-1):
    if sen[i] == ' ':
        cnt += 1
print(cnt)