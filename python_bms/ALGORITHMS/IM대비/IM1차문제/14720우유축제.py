N = int(input())
m_s = list(map(int,input().split()))
# 0: 딸기 1: 초코 2: 바나나 
yh_idx = 0
# 영학이의 인덱스가 1씩 증가하면서 m_s 를 지나간다. 
# 딸기우유0 을 먹은 후 초코우유 바나나우유 
cnt = 0 
milk = [0, 1, 2]
milk_idx = 0
# 영학이의 인덱스가 N 보다 작은 동안
while yh_idx < N:
    # 영학이의 위치가 딸기우유가게 0 이면 cnt 증가 , 영학 인덱스 증가, milk 인덱스 증가 
    if m_s[yh_idx] == milk[milk_idx]:
        cnt += 1
        milk_idx = (milk_idx + 1) % 3
        yh_idx += 1
    # 딸기우유가 아니면 인덱스만 증가 
    else:
        yh_idx += 1
print(cnt)
    

    
