line = "12+12"
for i in range(len(line)):
    if i.isdigit():
        # 0부터 9까지의 숫자라면 
        print("얘는 숫자임",int(i))
    else:
        print(i)