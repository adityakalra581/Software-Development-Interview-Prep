
some_data = [1,2,3,4,5,6,7,8]

## To fetch input in int entered with comma separation method.

# x = list(map(int,input().split(",")))


## Method1: Brute force

four_index = some_data.index(4)
seven_index = some_data.index(7)
    
num1 = 0
num2 = ""

# num1: addition of numbers in outer of 4 and 7
# num2: concatenate numbers in between 4 and 7 (including 4 and 7)

for i in range(four_index):
    num1 += some_data[i]

for i in range(seven_index+1,len(some_data)):
    num1  += some_data[i]

##NUM1 Done
#For NUM2

for j in range(four_index, seven_index+1):
    num2 += str(some_data[j])

## Final answer:

print("Output method 1: ",num1 + int(num2))
# ---------------------------------------------------------------------
## Method2:

number1 = sum(some_data[:some_data.index(4)]) + sum(some_data[some_data.index(7)+1:])
# print(number1)

sliced_list = some_data[some_data.index(4):some_data.index(7)+1]
number2 = ""

for i in sliced_list:
    number2 += str(i)

print("Output Method 2: ",number1 + int(number2))

# -----------------------------------------------------------------------


