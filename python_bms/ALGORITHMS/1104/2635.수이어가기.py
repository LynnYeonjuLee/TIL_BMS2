N = int(input())
temp = [N]
cnt_l = []
stan_len = 0
if N == 1:
    cnt_l = [1, 1, 0, 1] # 하하하하하ㅏ하하하 하하하하하하 
else:
    cnt_l = []
    for i in range(N):
        temp = [N]
        temp.append(i)
        while temp[-2]-temp[-1]>= 0:
            temp.append(temp[-2]-temp[-1])
            if stan_len < len(temp):
                stan_len = len(temp)
                cnt_l = temp
            
print(len(cnt_l))
for l in cnt_l:
    print(l,end=' ')
# 최대 개수의 수들이 여러 개일 때, 그중 하나의 수들만 출력하면 된다.??
