T = int(input())
 
def cal(num1, op, num2):
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 // num2
 
for a in range(1, T+1):
    stack_result = input().split()
    stack_result.pop()
    stack_operater = []
    for op in stack_result:
        if '0' <= op <= '9':
            stack_operater.append(op)
        else:
            if len(stack_operater) < 2:
                print('#{} error'.format(a))
                break
            num2 = stack_operater.pop()
            num1 = stack_operater.pop()
            stack_operater.append(cal(num1, op, num2))
    else:
        if len(stack_operater) != 1:
            print('#{} error'.format(a))
            continue
        result = stack_operater[0]
        print('#{} {}'.format(a, result))