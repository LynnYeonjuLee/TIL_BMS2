user_input = int(input())
count = 0
for i in range(1, user_input+1):
    count += i # 처음에  while 을 잘못써서 무한루프 !! 
    
print(count)