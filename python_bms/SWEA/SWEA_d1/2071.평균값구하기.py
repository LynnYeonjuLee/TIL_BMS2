T = int(input())
for test_case in range(1, T + 1):
    b = map(int, input().split())   # list(map(kkkkkk) 담아주거나 
    b = list(b)  #map은 리스트가 아니기 때문에 list 에 담아준다.  
    average = sum(b) / len(b)
    print('#{} {}'.format(test_case, round(average)))  # 처음에 test_case 를 T로 입력해서 오류남 