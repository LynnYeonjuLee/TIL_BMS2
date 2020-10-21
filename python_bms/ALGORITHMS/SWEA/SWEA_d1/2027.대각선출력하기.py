for i in range(5):
    for j in range(5):
        if i == j:
            print('#',end='')
        if i != j:
            print('+',end='')

    print( ) # 얘를 빼먹어서 자꾸 잘못 출력했다.