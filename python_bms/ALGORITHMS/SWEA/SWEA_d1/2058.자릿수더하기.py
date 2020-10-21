user_input = int(input())
result = 0
# for i in (0, len(user_input))
while user_input > 10:
    digit1 = user_input % 10 
    result += digit1
    user_input = user_input // 10
result += user_input
print(result)