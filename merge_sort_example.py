arr = [1, 3, 23433, 1232, 8832, 3902, 12, 9]


def mergeSort(arr):
  #check to make sure list has elements to sort
  if len(arr) > 1:
    #divide up our list into segments
    #get middle of list
    middle = len(arr) // 2
    left_side = arr[:middle]
    right_side = arr[middle:]
    #RECURSION TIME
    mergeSort(left_side)
    mergeSort(right_side)

    #count for both sides
    i = 0
    x = 0
    # count for our end list
    main_count = 0

    # while loop to check for segment size and run if segment not sorted
    while i < len(left_side) and x < len(right_side):
      if left_side[i] <= right_side[x]:
        arr[main_count] = left_side[i]
        i += 1
      else:
        arr[main_count] = right_side[x]
        x += 1
      
      # once check runs, increment main_count
      main_count += 1
    #check for final vals
    while i < len(left_side):
      arr[main_count] = left_side[i]
      i += 1
      main_count += 1
    while x < len(right_side):
      arr[main_count] = right_side[x]
      x += 1 
      main_count += 1

mergeSort(arr)
print(arr)