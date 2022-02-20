# Worst complexity: n^2

# Average complexity: n^2

# Best complexity: n

# Space complexity: 1

# Method: Exchanging

# Stable: Yes

# Class: Comparison sort

## COMPARE AND SWAP METHOD:

def bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

print(bubble([10,12,1,45,22,13]))

## OUTPUT:
## [1, 10, 12, 13, 22, 45]

## The second loop is executing a pass and the parent loop is responsible n passes.