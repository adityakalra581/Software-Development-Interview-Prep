# Problem link: https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
# Video referred: https://youtu.be/5o-kdjv7FD0

## It is given that possible number of steps that can be taken are 1,2 and 3. Not more than that.
## SO that's why 1,2 and 3 are the base cases.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

cache = dict()
def stepPerms(n):
    if n == 1:return 1
    if n == 2:return 2
    if n == 3:return 4
    if n not in cache:
        cache[n] = stepPerms(n-1)+stepPerms(n-2)+stepPerms(n-3)
    return cache[n]

## Correct but inefficient method
# def stepPerms(n):
#     if n==0 or n==1:
#         return 1
#     elif n==2:
#         return 2
#     elif n==3:
#         return 4
#     else:
#         return (stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3))

if __name__ == '__main__':

    s = int(input().strip())
    output = []
    for s_itr in range(s):
        n = int(input().strip())
        res = stepPerms(n)
        output.append(res)
    
    print("OUTPUT: ", output)