import sys
for line in sys.stdin:
    k_l = list(map(int,line.split()))
    minus1 = k_l[1]-k_l[0]
    minus2 = k_l[2]-k_l[1]
    if minus1 >= minus2:
        result = minus1-1
    elif minus1 < minus2:
        result = minus2-1
    print(result)