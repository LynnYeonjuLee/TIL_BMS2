C = int(input())
for i in range(C):
    # num = str(input())
    num_students = list(map(int,input().split()))
    count = 0
    for j in range(1, len(num_students)):
        score_avg = (sum(num_students)-num_students[0])/(len(num_students)-1) # num_students[0]을 해주지 않아서..... 오류떴음 
        if num_students[j] > score_avg:
            count +=1
    result = (((count / num_students[0]) * 100))
    print('{0:.3f}%'.format(result)) # 퍼센트 위치 잘 확인해주자 ㅎㅎㅎㅎ
