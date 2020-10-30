S = list(map(int,input()))
cnt0 = S.count(0)
cnt1 = S.count(1)
# 0 으로 바꾸는 횟수와 
# 1로 바꾸는 횟수를 나누어 생각해보자. ?
열고
while cnt0 != len(S) and cnt1 != len(S):
# 만약에 0의 개수가 1의 개수보다 많다면    
    if cnt0 > cnt1:
        cnt_flip = 0
    # 전체를 뒤집고     
        cnt_flip += 1  
        for i in range(len(S)):
            if S[i] == 0:
                S[i] = 1
            else:
                S[i] = 0
          
    # 1의 개수가 더 많으면 
    else:
        cnt_flip = 0
    # 그대로 둔다.  
        continue
print(cnt_flip)

