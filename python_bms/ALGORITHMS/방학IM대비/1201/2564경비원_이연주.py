garo, sero = map(int,input().split())
N = int(input()) # 상점의 개수
dir_list = []
p_list = []
for _ in range(N):
    direction, point = map(int,input().split()) # 상점 방향, 위치
    # 방향과 위치를 나누어서 담자
    dir_list.append(direction)
    p_list.append(point)
dong_d, dong_p = map(int,input().split()) # 동근이의 방향, 위치
dir_list.append(dong_d)
p_list.append(dong_p)


# 시계방향과 반시계방향을 나누어서 리스트에 담고 최소값을 골라낸다.
# 전체 길이
whole_length = 2*garo + 2*sero
p_location = []
# 시계방향으로 돌아 왼쪽 상단 끝에 도착할 때
for i in range(N+1):
    # 북쪽이면
    if dir_list[i] == 1:
        p_location.append(p_list[i])
    # 남쪽
    elif dir_list[i] == 2:
        p_location.append(2*garo + sero -p_list[i])
    elif dir_list[i] == 3:
        p_location.append(whole_length - p_list[i])
    else: # 4일 때
        p_location.append(garo + p_list[i])
result1 = []
result2 = []

for i in range(N):
    a = abs(p_location[-1] - p_location[i])
    result1.append(a)
    b = whole_length - a # a와 반대 방향인 값들
    result2.append(b)

min_result = []
for i in range(N):
    min_result.append(min(result1[i],result2[i]))
final_result = sum(min_result)
print(final_result)

# 동근이의 위치를 먼저 확인

