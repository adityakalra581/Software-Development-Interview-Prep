##

data = {"anchal":234567, "asha":89675, "ajay":9087}

keys = list(data.keys())
min_array = []
output = ""

for i in keys:
    length = len(i)
    value = str(data[i])
    for j in value:
        if int(j)<= length:
            min_array.append(j)
    max_element = max(min_array)
    

# print(min_array)