def str_rev(str):
    # str -> list
    arr = list(str)
    #swap
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-1-i] = arr[len(arr)-1-i] , arr[i]
    # list -> str
    str = ''.join(arr)
    return str

str = "Algorithm"
str1 = str_rev(str)
print(str1)



s = "Algorithm"
s = s[::-1]
print(s)


str2 = "Algorithm"
arr2 = list(str2)
arr2.reverse()
str2 = "".join(arr2)