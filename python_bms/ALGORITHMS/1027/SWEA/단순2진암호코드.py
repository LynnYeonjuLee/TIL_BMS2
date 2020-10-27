# # T = int(input())
# # for t in range(1, T+1):
# #     N, M = map(int,input().split())
# #     nums_list = []
# #     for n in range(N):
# #         nums = list(map(int,input().split()))
# #         nums_list.append(nums)

# #     print(nums_list)
# #     for i in range(len(nums_list)):
# #         if len(nums_list[i]) == 1:
# #             nums_list.remove(nums_list[i])
    
# # 1. 입력
# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int,input().split())
#     nums_list = []
#     for n in range(N):
#         nums = list(map(int,input().split()))
#         nums_list.append(nums)
# # 2. 이진수로 변경
#     bi2 = bin(bi)
#     tri2 = 
# # 3. 코드를 찾기
# #   3-1. 코드의 시작위치를 찾는다.
# #   3-2. 암호코드를 일반값으로 변경
# # 4. 검증 
# # 5. 출력

num = {
    '0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3', '0100011': '4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}
 
for t in range(int(input())):
    ans = 0
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    for i in range(N-5):
        temp_s = ''
        if ans: break
        for j in range(M-1, -1, -1):
            if ans: break
            if M-55 < 0: break
            if arr[i][j] == '0': continue
            temp_arr = arr[i][j-55: j+1]
            for z in range(8):
                temp_n = num.get(temp_arr[z*7:(z+1)*7], -1)
                if temp_n == -1: break
                else:
                    temp_s += temp_n
                    if len(temp_s) == 8:
                        for k in range(4):
                            if temp_arr != arr[i+k+1][j-55: j+1]: break
                        else:
                            check_n = 0
                            for k in range(0, 7, 2): check_n += int(temp_s[k])
                            check_n *= 3
                            for k in range(1, 8, 2):check_n += int(temp_s[k])
                            if not check_n % 10:
                                for k in range(8):
                                    ans += int(temp_s[k])
                                break
        
    print('#{} {}'.format(t+1, ans))
