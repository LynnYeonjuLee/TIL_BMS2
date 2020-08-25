T = input(int())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    result = []
    row_list = []
    column_list = []
    column_list2 = []
    for i in range(N):
        letters = input()
        row_list.append(letters)
        for i in range(len(letters)-M+1):
            if letters[i:M+i] == letters[i:M+i][::-1]:
                result.append(letters[i:M+i])
    for a in range(N):
        for b in row_list:
            column_list2 += b[a]
            column_list.append(column_list2)
            column_list2 = ''
    print(column_list)
    for letter in column_list:
        for j in range(len(letter)-M+1):
            if letter[j:M+j] == letter[j:M+j][::-1]:
                result.append(letter[j:M+j])

    print("#%d %s"%(tc, result[0]))

