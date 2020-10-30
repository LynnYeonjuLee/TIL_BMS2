# 미치겠어용.........ㅇ..ㅇ.ㅇ..ㅇ..ㅇ....
N = int(input())
bs = list(map(int,input().split()))
st = int(input())
# g_list1a = []
# g_list2a = []
# g_list1b = []
# g_list2b = []
cnt = 0

for _ in range(st):
    gen, num = list(map(int,input().split()))
    if gen == 1: # 남학생
        for i in range(len(bs)):
            if (i+1) % num == 0:
                if bs[i] == 0:
                    bs[i] = 1
                else:
                    bs[i] = 0
        # print(bs)
    else: # 여학생
        std = num - 1 # 기준점 
        new_std1 = std
        new_std2 = std
        # i1 = new_std-1
        # i2 = new_std+1
        while True:
            if 0 > new_std1 or new_std2 >= len(bs): # 벽체크 
                break
            else:
                new_std1 -= 1
                new_std2 += 1
                if 0 > new_std1 or new_std2 >= len(bs): # 벽체크 
                    break
                # if bs[new_std1] != bs[new_std2]:
                #     if bs[std] == 0:
                #         bs[std] = 1
                #     else:
                #         bs[std] = 0
                if bs[new_std1] == bs[new_std2]:
                    if bs[new_std1] == 0 and bs[new_std2] == 0:
                        bs[new_std1] = 1
                        bs[new_std2] = 1
                    else:
                        bs[new_std1] = 0
                        bs[new_std2] = 0
                else:
                    break
        
        if bs[std] == 0:
            bs[std] = 1
        else:
            bs[std] = 0
            # if bs[std] == 0:
            #     bs[std] = 1
            # else:
            #     bs[std] = 0
            # i1 -= 1
            # i2 += 1
            # if new_std1 == 0:
            #     pass
            # elif new_std2 == len(bs):
            #     pass
            # else:
            
        #     cnt += 1
        #     if new_std1 < 0 or new_std2 > len(bs):
        #         new_std1 += 1 
        #         new_std2 -= 1
        #         break

        # print(new_std1)
        # print(new_std2)
        # if cnt == 0: # 양 옆 스위치 상태가 다르다면 
        #     if bs[std] == 0:
        #         bs[std] = 1
        #     else:
        #         bs[std] = 0
        # else:
        #     for i in range(new_std1, new_std2+1):
        #         if bs[i] == 0:
        #             bs[i] = 1
        #         else:
        #             bs[i] = 0
        

        # if len(bs) // 2 > std:
        #     for i in range(0, num-1+num):
        #         g_list1a.append(bs[i])
        #     for j in range(num-1+num,len(bs)):
        #         g_list1b.append(bs[j])
        #     for k in range(len(g_list1a)):
                
        # else: 
        #     for i in range(std-(len(bs)-std), len(bs)):
        #         g_list2a.append(bs[i])
        #     for j in range(std-(len(bs)-std)):
        #         g_list1b.append(bs[j])
# print(g_list1a)
# print(g_list2a)
# print(g_list1b)
# print(g_list2b)
# for b in range(20):
#     print(bs[b],end=' ')
# print()
# if N <= 20:
#     for b in bs:
#     print(b,end=' ')
# else:
#     for b in bs:
for i in range(len(bs)):
    print(bs[i],end=' ')

    if (i+1) % 20 == 0:
        print()
'''
8
0 1 0 1 0 0 0 1
2
1 8
2 7


8
0 1 0 1 0 0 0 1
2
1 8
2 7
'''