# num = list(map(int,input().split()))
# sorted_num = sorted(num)
# i = len(num)//2 
# result = sorted_num[i]
# print(result)



# T = int(input())
#num = list(map(int,input().split()))
#for test_case in range(1, T + 1):
#   sorted_num = sorted(num)
#	i =len(num)//2 
#	result = sorted_num[i]
#	print(result)

#import statistics
#num = list(map(int,input().split()))
#result = statistics.median(num)
#print(result)


#T = int(input())
#num = list(map(int,input().split()))
#for test_case in range(1, T + 1):
 #   sorted_num = sorted(num)
#	i =len(num)//2 
#	result = sorted_num[i]
#	print(result)
import statistics
T = int(input())
num = list(map(int,input().split()))
for test_case in range(1, T + 1):
	result = statistics.median(num)
print(result)