numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

length = 0
for number in numbers:
    length += 1
median_idx = length // 2
sorted_numbers = sorted(numbers)
print(sorted_numbers[median_idx])