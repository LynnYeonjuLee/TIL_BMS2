
import sys
sys.stdin = open("2028종이자르기.txt")
dir_garo = []
dir_sero = []
garo, sero = map(int, input().split())
N = int(input()) # 점선의 개수
for n in range(N):
    direction, line_num = map(int, input().split())

    if direction == 0:
        dir_garo.append(line_num)
    else:
        dir_sero.append(line_num)
dir_garo.append(0)
dir_sero.append(0)
dir_garo.append(sero)
dir_sero.append(garo)
dir_garo.sort()
dir_sero.sort()
dir_garo.reverse()
dir_sero.reverse()
arr1= []
arr2=[]
# print(dir_garo)
for i in range(len(dir_garo)-1):


    arr1.append(dir_garo[i]-dir_garo[i+1])

for i in range(len(dir_sero) - 1):

    arr2.append(dir_sero[i] - dir_sero[i + 1])

max1 = max(arr1)
max2 = max(arr2)

print(max1*max2)
