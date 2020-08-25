T = int(input())
for test_case in range(1, T+1):
    words = str(input())
    words_list = list(words)
    same_letter_lst = []
    for i in range(1, len(words_list)-1):
        if words_list[0] == words_list[i]:
            if i != 1 and words_list[1] == words_list[i+1]:
                same_letter_lst.append(i)
    print('#{} {}'.format(test_case,same_letter_lst[0]))