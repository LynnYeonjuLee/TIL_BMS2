T = int(input())

for tc in range(1, T + 1):
    result_lst = []
    answer = 1
    str_input = str(input())
    str_lst = list(str_input)
    for i in range(0, len(str_lst)):
        if str_lst[i] == '(' or str_lst[i] == '{':
            result_lst.append(str_lst[i])
        elif str_lst[i] == ')' or str_lst[i] == '}':
            if not result_lst:
                answer = 0
                break
            P = result_lst.pop()
            if str_lst[i] == ')' and P != '(':
                answer = 0
            elif str_lst[i] == '}' and P != '{':
                answer = 0
    if result_lst:
        answer = 0
    print("#{} {}" .format(tc, answer))