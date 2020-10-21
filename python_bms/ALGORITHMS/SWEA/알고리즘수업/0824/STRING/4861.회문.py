# T = input(int())
# for tc in range(1, T+1):
#     N, M = map(int,input().split())
#     result = []
#     row_list = []
#     column_list = []
#     column_list2 = []
#     for i in range(N):
#         letters = input()
#         row_list.append(letters)
#         for i in range(len(letters)-M+1):
#             if letters[i:M+i] == letters[i:M+i][::-1]:
#                 result.append(letters[i:M+i])
#     for a in range(N):
#         for b in row_list:
#             column_list2 += b[a]
#             column_list.append(column_list2)
#             column_list2 = ''
#     print(column_list)
#     for letter in column_list:
#         for j in range(len(letter)-M+1):
#             if letter[j:M+j] == letter[j:M+j][::-1]:
#                 result.append(letter[j:M+j])

#     print("#%d %s"%(tc, result[0]))



# NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램
T = int(input())
for TC in range(1, T+1):
    arr = list()
    N, M = map(int,input().split())

    for i in range (N):#가로
        string = str(input())
        arr.append(string)
        for j in range(0,N-M+1):
            end = M+j
            if string[j:end] == string[j:end][::-1]:
                ans = string[j:end]
    #세로
    vertArr = list()

    for j in range(0,N):
        vertStr = str()
        vert = list()
        for i in range(0,N):
            vert.append(arr[i][j])
        vertStr = ''.join(vert)
        vertArr.append(vertStr)
        for k in range(0,N-M+2):
            end = M+k
            if vertStr[k:end] == vertStr[k:end][::-1] :
                ans = vertStr[k:end]
    
    print("#%d %s" %(TC,ans))