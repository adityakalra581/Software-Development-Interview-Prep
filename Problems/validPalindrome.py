s = "A man, a plan, a canal: Panama"

new_string = (''.join(char for char in s if char.isalnum())).lower()
reversedString = new_string[::-1]

if new_string == reversedString:
    print("true")
else:
    print("false")