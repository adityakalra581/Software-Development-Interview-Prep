
new = "my name is aditya"
temp = new.split()[::-1]
print("Reversed list: ",temp)
output = []


for i in temp:
    output.append(i)


print("final result:", " ".join(output))


