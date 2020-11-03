N = int(input())
os = list(map(int,input().split()))
o_result = [1]

for i in range(1, N):
    if os[i] == 0:
        o_result.append(i+1)
    else:
        # for j in range(0,os[i]):
            # o_result[j] += 1
        o_result.insert(i-os[i],i+1)
        # o_result.append(i+1)
for o in o_result:
    print(o,end=' ')
# print(o_result)
