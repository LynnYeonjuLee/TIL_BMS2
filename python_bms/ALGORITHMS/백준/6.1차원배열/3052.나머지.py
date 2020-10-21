
rmd_list = []
rmd = 0
for i in range(10):
    num = int(input())
    rmd = num % 42
    if rmd not in rmd_list:
        rmd_list.append(rmd)
print(len(rmd_list))

    #for j in range(10):
    #     rmd = num_list[j] % 42
    #     if rmd not in rmd_list:
    #         rmd_list.append(rmd)
    # 처음에 이중 for 문으로 생각해서 좀 시간이 걸렸다 ㅠㅡㅠ ! 


