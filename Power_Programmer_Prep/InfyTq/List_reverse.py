## Reverse a list of non duplicate characters:
# EG: INPUT: I,N,F,O,S,Y,S
# Output: YSOFNI

from audioop import reverse


data = list(map(str,input().split(",")))

#Method1: Brute force
temp = []
for i in data:
    if i not in temp:
        temp.append(i)
reversed_data = temp[::-1]
print("Output Method1: ", "".join(reversed_data))
#------------------------------------------------------------

#Method2: Using fromkeys function of dictionary

temp2 = list(dict.fromkeys(data))
reversed_data2 = temp2[::-1]
print("Output method2: ", "".join(reversed_data2))

