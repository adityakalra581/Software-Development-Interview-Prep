## add absolute difference of two elements of the array if it is unique for the array
## Solution reference: https://youtu.be/53VARW7rn88

## Math.gcd: https://www.w3schools.com/python/ref_math_gcd.asp  for Python 3.5 and above


## Just in case:
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

import math

length = int(input())
array = list(map(int,input().split(" ")))

ans = array[0]

for i in range(length):
    ans = gcd(ans,array[i])

ans_ = (max(array)//ans) % (math.pow(10,9)+7)

print(int(ans_))