w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

# 만약 벽이 없다면? 그대로 쭉 나감
# 시작점 p에서 벽을 몇번이나 만나는가? 홀수면 방향이 반전, 짝수면 그대로 
# 현위치 구하기 
# 짝수라면 왼쪽(아래)에서 이동하는 것이므로 남은 만큼만
# 홀수라면 오른쪽 (위쪽)에서 이동하는 것이므로 이동 거리만큼 빼주면 
# 벽에 부딪히는 횟수
a = (p + t) // w  
b = (q + t) // h

if a % 2 == 0: # 짝수
    x = (p + t) % w
else: # 홀수면
    x = w - ((p + t) % w)

if b % 2 == 0: # 짝수
    y = (p + t) % h
else: # 홀수면
    y = h - ((p + t) % h)

print(x, y)