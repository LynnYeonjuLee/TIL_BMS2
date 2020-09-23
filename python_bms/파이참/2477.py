K = int(input()) # 참외의 수
# a  방향 1- 동 2- 서 3- 남 4-북
# b 길이
temp = []
for tc in range(6):
    a, b = map(int, input().split())
    temp.append(b) # 방향은 버리고 길이만 받아옴

b_idx = 0
multi_max = 0
for i in range(6):
    multi = temp[i] * temp[(i+1)%6]
    if multi_max < multi:
        multi_max = multi
        b_idx = i
small_box = temp[(b_idx+3)%6] * temp[(b_idx+4)%6]

# 총 면적과 참외의 수를 곱해주면 결과값
result = (multi_max - small_box) * K
print('{}'.format(result))

