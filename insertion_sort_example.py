# INSERTION SORT EXAMPLE
arr = [1, 3, 23433, 1232, 8832, 3902, 12, 9]


for indx, elem in enumerate(arr):
  #setup initial holding variable
  element = arr[indx]
  count = indx
  #loop through our array
  while (count > 0 and arr[count - 1] > element):
    print(f'{count} is the current count')
    print(f'{element} is the current element')
    print(f'{arr[count-1]} is the current comparison element')
    #if true, run swtich
    arr[count] = arr[count - 1]
    count = count - 1
 
  arr[count] = element

print(arr)
