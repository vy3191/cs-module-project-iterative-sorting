testValues = [29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20]

def selection_sort(arr):
  sorted_list =  []
  for i in range(0, len(arr)):
    index_to_move = index_of_min(arr)
    # print(index_to_move)
    min_item = arr.pop(index_to_move)
    print(min_item)
    sorted_list.append(min_item)
    print("%-25s %-25s" %(arr, sorted_list))
  return sorted_list

def index_of_min(arr):
  min_index = 0
  for i in range(1,len(arr)):
    if arr[i] < arr[min_index]:
      min_index = i
  return min_index    

results = selection_sort(testValues)  
print(results)
