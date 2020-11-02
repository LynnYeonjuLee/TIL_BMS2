def merge(lst):
    cnt = 0
    if len(lst) <= 1:
        return lst, cnt
    else:
        l, l_cnt = merge(lst[ : len_lst//2])
        r, r_cnt = merge(lst[len_lst//2 : ])
        temp = [] 
        l_idx = r_idx = 0
        r_is_small = False
        for _ in range(len(lst)):
            if l_idx == len(l): 
                temp.append(r[r_idx]) 
                r_idx += 1       
            elif r_idx == len(r):
                temp.append(l[l_idx]) 
                l_idx += 1
                r_is_small = True 
            elif l[l_idx] <= r[r_idx]: 
                temp.append(l[l_idx])  
                l_idx += 1
            else: 
                temp.append(r[r_idx])
                r_idx += 1
        cnt = l_cnt + r_cnt
        if r_is_small: 
            cnt += 1
        return temp, cnt

def sorted_merge(lst):
    sorted_lst, cnt = merge(lst)
    return sorted_lst[N//2], cnt

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    print('#{}'.format(t), *sorted_merge(lst))