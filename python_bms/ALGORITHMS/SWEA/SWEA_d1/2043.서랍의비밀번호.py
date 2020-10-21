a, b = map(int,input().split())
count = 1

if a == b:
    print(count)
else:
    while  a > b:  
        count += 1
        b += 1
    print(count)
# for i in range(b, a-b+1):
#     if i == a:
#         count += 1
#         break
#     else:
#         count += 1
