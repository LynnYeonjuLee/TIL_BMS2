def itoa(num):
    x = num #몫
    y = 0  #나머지
    arr = []
    while x:
        y = x % 10
        x = x // 10
        arr.append(chr(y + ord('0')))
    arr.reverse()
    str = ''.join(arr)
    return str


x = 123
print(x, type(x))
str = itoa(x)
print(str, type(str))