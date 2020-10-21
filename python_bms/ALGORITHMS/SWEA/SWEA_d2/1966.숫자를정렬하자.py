T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    numbers = list(map(int,input().split()))
    srt_nums = sorted(numbers)
    result = ' '.join(map(str,srt_nums)) # 아무 생각없이 join을 썼더니 오류가 떴고 
                                         # int형 리스트를 조인하는 방법은 .join(map(str,리스트))

    print(f'#{test_case} {result}')