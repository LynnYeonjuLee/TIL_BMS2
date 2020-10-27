T = int(input())
for t in range(T):
    bi = list(input())
    tri = list(input())
    check = 0
    for i in range(len(bi)*2): 
        bi2 = bi[:]
        bi2[i//2] = str(i % 2) 
        a = ''.join(bi2)
        for j in range(len(tri)*3):
            tri3 = tri[:]
            tri3[j//3] = str(j % 3) 
            b = ''.join(tri3)
            if int(a,2) == int(b,3):
                print('#{} {}'.format(t+1,int(a,2)))
                check = 1
                break
        if check == 1:
            break

1697
2206
2589
2636
1012
1783
13305