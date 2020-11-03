# 이렇게 푸는게... 맞나요..?

N = int(input())
new_A = []
new_B = []
for _ in range(N):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    winner = ''
    new_A = A
    new_B = B
    new_A.remove(A[0])
    new_B.remove(B[0])
    if new_A.count(4) > new_B.count(4):
        winner = 'A'
    elif new_A.count(4) < new_B.count(4):
        winner = 'B'
    elif new_A.count(4) == new_B.count(4) and new_A.count(3) > new_B.count(3):
        winner = 'A'
    elif new_A.count(4) == new_B.count(4) and new_A.count(3) < new_B.count(3):
        winner = 'B'
    elif new_A.count(4) == new_B.count(4) and new_A.count(3) == new_B.count(3) and new_A.count(2) > new_B.count(2):
        winner = 'A'
    elif new_A.count(4) == new_B.count(4) and new_A.count(3) == new_B.count(3) and new_A.count(2) < new_B.count(2):
        winner = 'B'
    elif new_A.count(4) == new_B.count(4) and new_A.count(3) == new_B.count(3) and new_A.count(2) == new_B.count(2) and new_A.count(1) > new_B.count(1):
        winner = 'A'
    elif new_A.count(4) == new_B.count(4) and new_A.count(3) == new_B.count(3) and new_A.count(2) == new_B.count(2) and new_A.count(1) < new_B.count(1):
        winner = 'B'
    if new_A.count(4) == new_B.count(4) and new_A.count(3) == new_B.count(3) and new_A.count(2) == new_B.count(2) and new_A.count(1) == new_B.count(1):
        winner = 'D'
    print(winner)