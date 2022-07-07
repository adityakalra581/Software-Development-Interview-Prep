## Only = 

lst1 = [1,2,3]
lst2 = lst1

## Before change
print(lst2)
## [1, 2, 3]

lst1[0] = 100

## After change
print(lst2)
## [100, 2, 3]

# --------------------------------------------

## Shallow Copy: If we have 1d list the changes in one list won't change the other, but 2d list will be altered with alteration in the original list


lst1 = [1,2,3]
lst2 = lst1.copy()

## Before change
print(lst2)
## [1, 2, 3]

lst1[0] = 100

## After change
print(lst2)
## [1, 2, 3]
## There is no change in second list

print("-------------------------------------")
lst1.append([4,5,6])
print("List1: ",lst1)
print("List 2 After appending: ",lst2)

## Output:
# List1:  [100, 2, 3, [4, 5, 6]]
# List 2 After appending:  [1, 2, 3]

print("------------------------------------")

## Let's try another use case:

temp1 = [[1,2,3],[4,5,6]]
temp2 = temp1.copy()

print("before altering element: ",temp2)

temp1[1][0] = 1000
print("After altering element List 1: ",temp1)
print("After altering element List 2: ",temp2)
print("------------------------------------")


# --------------------------------------
## Output: 
# before altering element:  [[1, 2, 3], [4, 5, 6]]
# After altering element List 1:  [[1, 2, 3], [1000, 5, 6]]
# After altering element List 2:  [[1, 2, 3], [1000, 5, 6]]

# ---------------------------------------------------------------------------

## Deep Copy: The copied list will never be altered with alterations in original list.

import copy

lst1 = [1,2,3]
lst2 = copy.deepcopy(lst1)

## Before change
print(lst2)
## [1, 2, 3]

lst1[0] = 100

## After change
print(lst2)
## [1, 2, 3]
## There is no change in second list

## Let's try another use case:

temp1 = [[1,2,3],[4,5,6]]
temp2 = copy.deepcopy(temp1)

print("before altering element: ",temp2)

temp1[1][0] = 1000
print("DeepCopy After altering element List 1: ",temp1)
print("DeepCopy After altering element List 2: ",temp2)

## Output:

# before altering element:  [[1, 2, 3], [4, 5, 6]]
# DeepCopy After altering element List 1:  [[1, 2, 3], [1000, 5, 6]]
# DeepCopy After altering element List 2:  [[1, 2, 3], [4, 5, 6]]


