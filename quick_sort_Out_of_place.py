
# take the first element as pivot
def qsort(arr):
  pivot=arr[0]
  low_list=[]
  high_list=[]
  for elem in arr:
    if elem < pivot:
      print(elem)
      low_list.append(elem)
    elif elem>pivot:
      high_list.append(elem)
  low_list.append(pivot) # so that the pivot is centered
  #print(low_list)
  #print(high_list)
  return low_list+high_list

fuckall=[16,1,26,23,12,19,13,14,12,11,6,54,32,45]
print(qsort(fuckall))