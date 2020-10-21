# 부분집합의 합 
T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int,input().split()))
    sum_num = 0
    cnt = 0
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
     # 출력할 결과 값을 넣을 리스트 
    for i in range(1<<len(numbers)):
        result = []
        for j in range(len(numbers)):
            if i & (1 << j): # 처음에 1 을 i 라고 써서 자꾸 오류남 ㅜㅠㅠ
                result.append(numbers[j])
            
        if len(result) == N :
            if sum(result) == K:
                cnt += 1
    print(f'#{tc} {cnt}')
    