T = int(input())

numbers = list(map(int,input().split()))
new_nums = sorted(numbers) 
print('{} {}'.format(new_nums[0], new_nums[-1]))