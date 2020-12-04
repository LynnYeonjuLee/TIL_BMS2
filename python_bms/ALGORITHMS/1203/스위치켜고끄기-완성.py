N = int(input())
bulbs = list(map(int,input().split()))
s_N = int(input())
s_list = []
for _ in range(s_N):
    s = list(map(int,input().split()))
    s_list.append(s)
    if s[0] == 1:
        for i in range(N):

            if (i + 1) % s[1] == 0:
                if bulbs[i] == 1:
                    bulbs[i] = 0
                else:
                    bulbs[i] = 1
    else:

        start = s[1] - 1  # 2
        end = s[1] - 1  # 2
        # print(start)
        # print(end)
        if bulbs[start] == 1:
            bulbs[start] = 0
            bulbs[end] = 0
        else:
            bulbs[start] = 1
            bulbs[end] = 1

        while start > 0 and end < N - 1:
            start -= 1  # 1 0
            end += 1  # 3 4
            if bulbs[start] == bulbs[end]:
                if bulbs[start] == 1:
                    bulbs[start] = 0
                    bulbs[end] = 0
                else:
                    bulbs[start] = 1
                    bulbs[end] = 1
            else:
                break
# print(m)
# print(f)
for i in range(len(bulbs)):
    print(bulbs[i], end=' ')
    if (i+1) % 20 == 0:
        print()