
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.

# 예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.
T = int(input())
for t in range(1, T+1):
    N = input()
    num_dict = {'ZRO': 0, 'ONE': 0, 'TWO': 0, 'THR': 0, 'FOR': 0, 'FIV': 0, 'SIX': 0, 'SVN': 0, 'EGT': 0, 'NIN': 0}
    num_list = input().split()
    result = ''
    for num in num_list:
        num_dict[num] += 1

    for key, value in num_dict.items():
        temp = ' '.join([key] * value)
        result += temp + ' '
    
    print("#{}".format(t))
    print(result[:len(result) - 1])