cnt = 0
for i in range(4):
    chess_w = list(map(str,input()))
    chess_b = list(map(str,input()))
    
    for j in range(0,8,2):
        if chess_w[j] == 'F':
            cnt += 1
        else:
            pass
    for k in range(1, 8, 2):
        if chess_b[k] == 'F':
            cnt += 1
print(cnt)
        
        
