# T = input(int())
# for tc in range(1, T+1):
#     P = input()
#     T = input()

# pp, tp 하고 초기화
# found = False
# #while 못받은 동안 and TP가 범위를 벗어나는 경우:
# while not found and tp < len(T) and pp < len(P):
#     if p[pp] == T[tp]:
#         pp += 1
#         tp += 1
#         #if pp가 마지막에 오면 : 
#         if pp == len(P):
#             found = True
            
#     else:
#         pp = 0
#         tp = 

#     if 찾은경우: 
#         print('1')
#     else:
#         print('0')
# T = input(int())
# for tc in range(1, T+1):
#     str1 = input()
#     str2 = input()

#     result = 0
#     for i in range(len(str2)-len(str1)+1):
#         if str2[i:i+len(str1)] == str1:
#             result = 1

#     print('#%d %s'%(tc, result))



T = int(input())
for TC in range(1, T+1):
    str1 = str(input())
    str2 = str(input())

    if str1 in str2:
        print("#%d %d" %(TC,1))
    else :
        print("#%d %d" %(TC,0))