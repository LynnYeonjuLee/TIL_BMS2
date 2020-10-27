T = int(input())
for t in range(1, T+1):
    arr = [0] * 10
    N = int(input())
    cards = list(map(int,input()))
    
    for card in cards:
        arr[card] += 1
    max_card = 0    
    max_count = 0
    for i,value in enumerate(arr):
        if max_card <= value:
            max_card = value 
            max_count = i
    print('#{} {} {}'.format(t, max_count, max_card))