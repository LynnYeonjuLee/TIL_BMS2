N = int(input())
# N 은 1보다 크고 100보다 작거나 같은 자연수 
# 1인 계단수가 몇 개 있는지 궁금 

# 깊이가 100이라서 재귀가 충분히 가능 1000이상이면 재귀 X -> deque q stack 

# 문자열을 만들 때, 만든 문자열    size, 모양, 
# cnt = 0
# def dfs(string):
#     global cnt 
#     if len(string) == N:
#         cnt += 1
#         return 
#     if len(string) ==0:
#         for i in range(1, 10):
#             newstring = str(i)
#             dfs(newstring)
#         return
#     num = int(string[len(string)-1]) # 맨 마지막 자리 수 
#     for i in [-1, 1]:
#         newnum = num + i
#         if newnum < 0 or newnum > 9:
#             continue
#         newstring = string + string(newnum)
#         dfs(newstring)
# # dfs('')
# dfs(str())
# print(cnt % 1000000000)
# 런타임에러 
# 수학으로 풀자룽 

# 0 과 9 는 한개 1~8 은 2개씩 


arr = [0]+[1]*9
# print(arr)
# newarr = []
for i in range(N-1):
    newarr = [0]*10
    for j in range(10):
        # print(newarr)
        if j == 0:
            newarr[1] += arr[0]
            # print(arr[0])
            # print(newarr[1])
        elif j == 9:
            newarr[8] += arr[9]
        else:
            newarr[j-1] += arr[j]
            newarr[j+1] += arr[j]
        newarr[j] %= 1000000000
    arr = newarr
    # print(newarr)
print(sum(arr)%1000000000)
# if N == 1:
#     print(9)
# else:
#     sum = 15
#     for i in range(N-2):
#         sum *= 2
#         sum %= 1000000000
#     result = (sum + 2)%1000000000
#     print(result)






    
