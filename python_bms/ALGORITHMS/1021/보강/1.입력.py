# 입력

# arr = [[1]* 7 for _ in range(7)]
# print(arr)


N = int(input())
# for i in range(N):
#     nums = list(map(int,input())
#     arr.append(nums)


arr = [list(map(int, input())) for _ in range(N)]


# nums = list(input())

# 1 1 1 1 1
print(list(input().split()))
# split 을 하는 순간 리스트 형태로 바뀌기 때문에 list를 안써줘도 됩니다. 

# 1 2
R, C = map(int,input().split())
# 1 2 3 을 넣으면 오류가 난다. 왜 그로카? -> 세 개를 받을 변수가 없어서

arr = list(map(int, input().split()))
arr[0]
arr[1]
arr[2]
