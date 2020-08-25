T = int(input())
for test_case in range(1, T+1):
    word = list(input())
    for i in range(len(word) // 2):
        if word[i] != word[-1 -i]:# 이부분 
            result = 0
        else:
            result = 1
    print(f'#{test_case} {result}')