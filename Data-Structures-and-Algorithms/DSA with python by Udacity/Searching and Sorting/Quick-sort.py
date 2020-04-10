"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

# I'll choose Pivot Last element of the array.
def quicksort(array,low,high):
    # def quicksort(T,low,high):
    # low= 0
    # high = len(array)-1
    if low<high:
        p=partition(array,low,high)
        quicksort(array,low,p-1)
        quicksort(array,p+1,high)
    return array
        
def partition(array,low,high):
    i=low-1
    pivot=array[high]
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
            array[j],array[i]=array[i],array[j]
    array[i+1],array[high]=array[high],array[i+1]
    return i+1
    
    
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test,0,9))

## OUTPUT:
## [1, 3, 4, 6, 9, 14, 20, 21, 21, 25]