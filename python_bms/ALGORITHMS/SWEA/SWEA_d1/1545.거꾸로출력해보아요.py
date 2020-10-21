user_input = int(input())
result = []

while user_input >= 0:
    result.append(user_input)
    user_input -= 1

result = ' '.join(map(str, result))
print(result)

print(list(map(str, result)))