## Fetch numbers from a string and create a largest even number and if even number is not possible then return -1

##Input: bsdjhbsd@6711tY88
##Output: 887116

from curses.ascii import isdigit
from os import remove

num1 = ""
data = list(map(str,input().split(" ")))

for i in data:
    if i.isdigit():
        num1 += i

temp = list(num1[::-1])
number = int("".join(temp))

if number%2==0:
    print(number)
else:
    for i in range(len(temp)-1,-1,-1):
        if int(temp[i])%2==0:
            temp_even = temp[i]
            temp.remove(temp[i])
            temp.append(temp_even)
            print("".join(temp))
            break
    else:
        print("-1")
