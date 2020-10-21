# 문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
T = int(input())

for tc in range(1, T + 1):
    string = str(input())
    i=0
    while 1:
        if i == len(string)-1: # 한글자면 빠져나오고 
            break
        if string[i] == string[i+1]:
            str1 = string[0:i]
            str2 = string[i+2:]
            string = str1 + str2
            i=0
        else:
            i += 1

    print("#{} {}" .format(tc, len(string)))