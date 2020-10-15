N = int(input())
for i in range(N):
    answers = list(map(str,input()))
    cnt = 0
    mark = 0
    for j in range(len(answers)):
        if answers[j] == 'O':
            mark += 1
            cnt += mark
        else: 
            mark = 0
            cnt += mark
    print(cnt)