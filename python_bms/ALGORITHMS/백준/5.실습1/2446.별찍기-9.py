# n = int(input())
# star = ''
# star_list = []
# for i in range(n+1, 0, -1):
#     star = '*' * (2*i -1)
#     # for j in range(0,2*n):
#     #     pass
# # for i in range(1,n):

# 별이 2n-1개 만큼 있다. 
# 2n-1 층 
# 별이 두개씩 감소 
# n-1층 까지 줄어들고 다시 n 만큼 늘어난다. 
# 공백은 왼쪽만 줘도 된다 ! 하나씩 바뀐다. 

n = int(input())
star = '*' * (2*n-1)
blank = ' '

for i in range(n-1):
    print(blank*i+star[2*i:])
for i in range(n-1, -1, -1): # 이 부분 다시 보기 !
    print(blank*i+star[2*i:])
