import sys

T = int(sys.stdin.readline())
for test_case in range(1, T+1):
    A, B = map(int,sys.stdin.readline().split())
    print(f'{A + B}')

# input 대신 sys.stdin.readline을 사용하는 문제! 
