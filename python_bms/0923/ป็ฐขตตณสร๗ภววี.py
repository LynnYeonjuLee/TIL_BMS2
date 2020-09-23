# T = int(input())
# for tc in range(1, T+1):
#     N, M, K = map(int, input().split())
#
#     for i in range(M): #
#         for j in range(N):
#             dnts = [[map(int,input().split())]*]

T = int(input())
for tc in range(1, T + 1):
    # 입력
    # 행, 열, 테두리 한 변의 길이
    # 행열, 가운데 좌표, 답을 저장해둘 빈 배열
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = []
    # n-k+1만큼 배열을 돌면서 ex) n = m = 3일 경우에 1번, n = m = 4일 경우 각 2번씩 ...
    for i in range(n - k + 1):
        for j in range(m - k + 1):

            # 사각형 전체 합을 저장해줄 변수 temp1
            temp1 = 0
            for y in range(k):
                for x in range(k):
                    temp1 += arr[i + y][j + x]
            # 테두리가운데부분 저장해줄 변수 temp2
            temp2 = 0
            for y in range(k - 2):
                for x in range(k - 2):
                    temp2 += arr[i +y + 1][j + x + 1]

            # 구해진 사각 테투리의 합에 가운데부분의 값을 빼준다. (도너츠 모양)
            # 최종 값을 res에 저장
            temp = temp1 - temp2
            res.append(temp)

    # res에 값이 하나밖에 없을때, 0을 출력
    if len(res) <= 1:
        print("#{} {}".format(tc, 0))
    else:
        print("#{} {}".format(tc, max(res) - min(res)))