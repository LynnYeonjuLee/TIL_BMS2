N, K = map(int,input().split())
f = []
f1 = []
m = []
m1 = []
cnt = 0
for _ in range(N):
    S, Y = map(int,input().split())
    if S == 0: # 여학생
        f.append(Y)
        if Y in f1:
            continue
        else:
            f1.append(Y)
    else: # 남
        m.append(Y)
        if Y in m1:
            continue
        else:
            m1.append(Y)
for f_y in f1:
    if f.count(f_y) % K == 0:
        cnt += (f.count(f_y) // K)
    else:
        cnt += (f.count(f_y) // K)
        cnt += 1
for m_y in m1:
    if m.count(m_y) % K == 0:
        cnt += (m.count(m_y) // K)
    else:
        cnt += (m.count(m_y) // K)
        cnt += 1
print(cnt)