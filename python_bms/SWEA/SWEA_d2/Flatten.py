for test_case in range(1, 11):
    dump = int(input())
    boxes = list(map(int,input().split()))
    boxes.sort()
    for _ in range(dump): # _: 이 값을 쓰지않고 돌리기만 하겠따~~~~! 승준이가 for 문에서만 당장은 쓰라고 함
        boxes[0] += 1
        boxes[-1] -= 1
        boxes.sort()
    print('#{} {}'.format(test_case, boxes[-1]-boxes[0]))