def binary_search(element, some_list):
    start_idx = 0
    end_idx = len(some_list) - 1
    
    while start_idx <= end_idx:
        midpoint = (start_idx + end_idx) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_idx = midpoint - 1
        else: 
            start_idx = midpoint + 1
            
    return None
  

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))