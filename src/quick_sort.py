testValues = [29, 100, 1, 2, 57, 28, 88, 3, 50, 67, 37, 1, 32, 20]

def quick_sort(arr):
  #base case
  if len(arr) <= 1:
    return arr
  left_half = []
  right_half = []
  pivot = arr[0]

  for value in arr[1:]:
    if value < pivot:
      left_half.append(value)
    else:
      right_half.append(value)  

  return quick_sort(left_half)+[pivot]+quick_sort(right_half)



results = quick_sort(testValues)  
print(results)
