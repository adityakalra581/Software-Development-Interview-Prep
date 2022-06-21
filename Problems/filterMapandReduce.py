## List comprehension function: 

from typing import Iterator


lst = [1,2,3,4,5]

### Case 1: Create a list which is squared of each number

lst1 = [x*2 for x in lst]
print(lst1)

### Output:0.. [2, 4, 6, 8, 10]

### Case 2: Create a list which check another list: if iterator is even put 0 else put 1

lst2 = [ 1 if x%2==0 else 0 for x in lst]
print(lst2)
### Output: [0, 1, 0, 1, 0]

## Lambda Function with Map Function:
'''
Map takes two arguments:
1. function
2. Iterator

The map() function is a higher-order function. As previously stated, this function accepts another function and a
sequence of ‘iterables’ as parameters and provides output after applying the function to each iterable in the sequence. It has the following syntax:

'''

lst3 = list(map(lambda x: x*2 , lst))
print(lst3)

### Output: [2, 4, 6, 8, 10]
