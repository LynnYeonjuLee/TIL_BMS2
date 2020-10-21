import copy

x = 10
y = x
print(x, y)
y = 20
print(x, y)

AAA = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
BBB = AAA
print(AAA, BBB)
BBB[1][1] = 3
print(AAA, BBB)
CCC = copy.deepcopy(AAA)
CCC[1][1] = 5
# 딥카피
for i in range(3):
    for j in range(3):
        BBB[i][j] = AAA[i][j]


# 인덱스가 아직 헷갈린다면 회전하는 문제와 좌표 계산하는 문제를 잘 보자 
