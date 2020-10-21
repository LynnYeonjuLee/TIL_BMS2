a, b = map(int,input().split())
quotient = a // b
remainder = a % b 
q = str(quotient)
r = str(remainder)
result = (q + ' ' + r)

print(result)