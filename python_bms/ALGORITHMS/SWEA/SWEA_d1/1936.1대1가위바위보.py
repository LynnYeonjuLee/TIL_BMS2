a, b = map(int,input().split())
if a < b:
    if a == 1 and b == 3:
        result = 'A'
    else: 
        result = 'B'
else: 
    if a == 3 and b == 1: 
        result = 'B'
    else: 
        result = 'A'
print(result)
