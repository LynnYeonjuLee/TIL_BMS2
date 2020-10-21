# T = int(input())
# b, c = list(map(int, input().split()))
# result = []
# for test_case in range(1, T + 1):
# 	for i in b:
#     	result.append(ord(i))
#         print(result,end='')
alphabet = list(input())      
result = ''
for i in alphabet:
    number = ord(i) - 64
    result += str(number) + ' '
print(result)