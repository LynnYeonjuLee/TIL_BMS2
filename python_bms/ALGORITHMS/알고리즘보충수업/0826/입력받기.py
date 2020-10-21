# 1, 2 
# a , b = map(int,input().split())


line=input()
print(type(line), line)

line = input().split()
print(type(line), line)


R, C = int(input().split())
arr = [list(map(int,input().split())) for _ in range(R)]

