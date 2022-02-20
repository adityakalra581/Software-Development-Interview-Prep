# Problem Link: https://www.hackerrank.com/challenges/coin-change/problem
# Solution reference: https://youtu.be/4S5x4SF4fsM

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n == amount
#  2. LONG_INTEGER_ARRAY c == list of coins

def getWays(n, c):
    # Write your code here
    
    numWays = [1] + [0]*n
    
    for coin in c:
        for i in range(coin,n+1):
            numWays[i] += numWays[i-coin]
            
    return numWays[n]
    
## Function to find minimum no. of coins to get to the amount

def minWays(n, c):
    
    minWays = [float('inf') for _ in range(n+1)]
    minWays[0] = 0

    for i in range(len(minWays)):
        for coin in c:
            if i-coin >= 0:
                minWays[i] = min(minWays[i], minWays[i-coin]+1)
            
    return -1 if minWays[-1] == float('inf') else minWays[-1]
    



n = int(input())

c = list(map(int, input().rstrip().split()))

# Print the number of ways of making change for 'n' units using coins having the values given by 'c'

ways = getWays(n, c)
minWay = minWays(n,c)
print("Total number of ways to make ",ways)
print("Minimum number of ways to make ",minWay)



