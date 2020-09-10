testValues = [29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20]

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  middle_index = len(arr) // 2
  left_arr = merge_sort(arr[:middle_index])
  right_arr = merge_sort(arr[middle_index:])
  sorted_value = []
  left_index = 0
  right_index = 0
  while left_index < len(left_arr) and right_index < len(right_arr):
    if left_arr[left_index] < right_arr[right_index]:
      sorted_value.append(left_arr[left_index])
      left_index += 1
    else:
      sorted_value.append(right_arr[right_index])  
      right_index += 1
  sorted_value += left_arr[left_index:]    
  sorted_value += right_arr[right_index:]
  return sorted_value

results = merge_sort(testValues)  
print(results)
