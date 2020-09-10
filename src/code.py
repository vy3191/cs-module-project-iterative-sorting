
testValues = [29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20]

def selection_sort(arr):
  sorted_list = [] 
  while len(arr) > 0:
    min_value = arr[0]
    for element in range(len(arr)):
      if arr[element] < min_value:
        min_value = arr[element]
    arr.remove(min_value)
    # if not min_value in sorted_list:
    sorted_list.append(min_value)
   
  return sorted_list

results = selection_sort(testValues)  
print(results)