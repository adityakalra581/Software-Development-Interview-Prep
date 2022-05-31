##Finding duplicates in an array and probably their count.

temp = [10,20,20,88,39,77,8,9,18,77]
output = {}

for i in temp:
    if i not in output.keys():
        output[i] = 1
    else:
        output[i] += 1

print(output)