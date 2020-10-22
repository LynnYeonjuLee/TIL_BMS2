# 기준을 잡는 것이 중요하다. 
# 1. 조건 : 회의가 일찍 끝나야 한다. 
# 2. 조건 : 
# 따라서, 끝나는 순서대로 정렬을 시켜보자 
N = int(input())
arr = []
for _ in range(N):
    start_end = list(map(int,input().split()))
    arr.append(start_end)
for i in range(len(arr)):
    arr[i][0], arr[i][1] = arr[i][1], arr[i][0]
arr.sort()
end_now = arr[0][0]
result = []
# answer = 1
result.append(arr[0]) # 첫번째 끝 값 
for i in range(1,len(arr)):
    if arr[i][1] >= end_now:
        result.append(arr[i])
        end_now = arr[i][0]
        # answer += 1
print(len(result))
# print(answer)


