## Find the second highest element in a list:

temp = [10,20,20,88,39,77,8,9,18,77]
input = list(set(temp))
print("Unique element list: ",input)

## with inbuilt functions:

input.sort()
print("The second highest element using sort function: ",input[-2])

# ---------------------------------------------------------------------------
## Without inbuilt functions:

print("--------------------------------------------------")
print("List:",input)
maximum = max(input[0],input[1])
print("max of list:",maximum)
secondMax = min(input[0],input[1])
print("min of list:",secondMax)
n = len(input)

for i in range(2,n):
    if input[i]>maximum:
        secondMax = maximum
        maximum = input[i]
    elif input[i]>secondMax:
        secondMax = input[i]

print("The second highest element without using inbuilt functions: ",secondMax)