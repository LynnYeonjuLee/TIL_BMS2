N, X = map(int,input().split())
x_list = list(map(int,input().split()))
result = ''
for x in x_list:
    if x < X:
        result = result + str(x)+' '
print(result)
