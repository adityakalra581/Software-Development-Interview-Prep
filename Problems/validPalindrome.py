s = "A man, a plan, a canal: Panama"

new_string = (''.join(char for char in s if char.isalnum())).lower()
reversedString = new_string[::-1]

if new_string == reversedString:
    print("true")
else:
    print("false")

# ---------------------------------------
#Without inbuilt functions:
data = "NITISH"
length = len(data)
temp = []
for i in range(length-1,-1,-1):
    temp.append(data[i])

reversed_data = ''.join(temp)

if data == reversed_data:
    print("True")
else:
    print("false")