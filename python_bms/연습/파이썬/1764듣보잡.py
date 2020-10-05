import sys

N, M = list(map(int,input().split()))
list_h = set() 
list_s = set()

for i in range(N):
    never_h = sys.stdin.readline().strip()
    list_h.add(never_h)
for j in range(M):
    never_s = sys.stdin.readline().strip()
    list_s.add(never_s)
result = list(list_h&list_s)
print(len(result))
for i in sorted(result): # 알파벳 순서대로 출력해주는 것이기 때문에 정렬을 해주는 것을 까먹으면 안된다. 
    print(i)