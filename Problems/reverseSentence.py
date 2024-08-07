
new = "my name is aditya"
temp = new.split()[::-1] #split helping to segaragate the words and revese the order not words
temp2 = new[::-1]
print("Reversed list: ",temp)
print("Reversed list 2: ",temp2) ## This will reverse each word
output = []


for i in temp:
    output.append(i)


print("Reverse sentence final result:", " ".join(output))


