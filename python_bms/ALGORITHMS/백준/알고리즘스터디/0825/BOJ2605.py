# 첫번째 학생은 0번을 받아 제일 앞에 줄을 선다
# 두번째 학생은 0번 또는 1번 둘 중 하나의 번호 
#   if 0번을 ㄷ뽑으면 그 자리에 그대로 있고 1번을 뽑으면 바로 앞의 학생 앞으로
# 세번째 학생은 0,1,2 중 하나의 번호를 뽑는다. 그리고 뽑은 번호만큼 앞자리로 
# 마지막 학생까지....

# 각자 뽑은 번호는 자신이 처음에 선 순서보다는 작은 수
T = int(input())
order_nums = list(map(int,input().split()))
result = []
for i, order_num in enumerate(order_nums):
    result.insert(len(result)-order_num, str(i+1))
print(' '.join(result))
        
