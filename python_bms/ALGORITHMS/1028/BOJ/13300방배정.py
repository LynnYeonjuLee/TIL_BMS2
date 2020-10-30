N, K = map(int,input().split())
m = []
f = []
for _ in range(N):
    gen, grade = map(int,input().split())
    if gen == 0:
        f.append(grade)
    else:
        m.append(grade)
    
new_m = sorted(m)
new_f = sorted(f)
print(new_m)
print(new_f)
cnt = 0
for nm in new_m:
    if new_m.count(nm) > 2:
        cnt += 1
        new_m.remove(nm)
        new_m.remove(nm)
    elif new_m.count(nm) == 2:
        cnt += 1
        new_m.remove(nm)
        new_m.remove(nm)
    else:
        cnt += 1
        new_m.remove(nm)
    cnt += len(new_m)

print(new_m)
print(new_f)
print(cnt)
