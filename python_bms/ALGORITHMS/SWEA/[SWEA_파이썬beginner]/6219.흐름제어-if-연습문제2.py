n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(f'{i}(은)는 {n}의 약수입니다.')
        if i == 1 and i == n:
            print(f'{n}(은)는 {}')

