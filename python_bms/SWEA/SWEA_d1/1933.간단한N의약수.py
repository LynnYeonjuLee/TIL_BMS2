user_input = int(input())
result = []
for i in range(1, user_input+1):
    if user_input % i == 0:
        result.append(i)        

result = ' '.join(list(map(str, result)))
    
print(result)
