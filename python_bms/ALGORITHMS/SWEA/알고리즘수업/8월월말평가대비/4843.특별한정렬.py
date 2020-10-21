T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = [] # 우리가 구하고자 하는 정렬된 값들을 넣을 리스트 result
    new_nums = sorted(numbers) # 정렬을 우선 한 번 해준다. 
    # 인덱스를 앞에서 뒤로 왔다갔다 하며 다시 '특별한 정렬' 을 하겠다. 
    for i in range(int(len(new_nums)/2)): #인덱스 활용 
        result.append(new_nums[-1])
        del new_nums[-1]
        result.append(new_nums[0])
        del new_nums[0]
    print(f"#{tc} {' '.join(map(str, result[:10]))}") # 10개 까지만 출력 !!!