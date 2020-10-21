N, M = map(int, input().split())
mylist = [0 for _ in range(N)]
for i in range(N):
    mylist.append(list(map(int,input().split())))
print(mylist)