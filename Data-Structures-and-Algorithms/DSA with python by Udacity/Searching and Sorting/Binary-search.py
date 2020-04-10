
## Implementation of Binary Search:

## Assumptions:

# 1. List is sorted in Ascending order
# 2. No duplicate integers are present.

## PSUEDO CODE: 
# 1. Check the mid point of the array. If the value you are searching for is smaller or greater than that.
# [ here head = 0 and tail is the end of list]
# 2. Shift your head and tail accordingly.
#     - If list[mid] == Value
#     then return mid
#     - elif list[mid]< Value
#     shift head to mid + 1
#     - else:
#     shift tail to mid - 1


def binary_search(input_array, value):
    
    head = 0
    tail = len(input_array)-1
    while head <= tail:
        half = int((head+tail)/2)
        if input_array[half] == value:
            return half
        elif input_array[half] < value:
            head = half+1 
        else:
            tail = half - 1
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
test_val3 = 0
test_val4 = 26
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, test_val3))
print(binary_search(test_list, test_val4))


## OUTPUT:
# -1
#  4
# -1
# -1

# **********************************