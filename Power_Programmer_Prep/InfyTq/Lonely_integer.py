data = list(map(int,input().split(" ")))
print("Initial data", data)
count = dict()

for i in data:
    if i in count.keys():
        count[i] += 1
    else:
        count.update({i:1})

print("Data and count: ",count)

for value,count in count.items():
    if count == 1:
        lonely_integer = value

print("Lonely integer: ", lonely_integer)
