#The join() method is a string method and returns a string
# in which the elements of sequence have been joined by str separator.


a=['1','2','3','4','5']
b=['Aditya','Kalra','is','broke']

s=" "
m="-"

# Syntax of joining a connector to a list(String based) and removing parenthesis
#var=connector.join(list_name)


print(s.join(a))
print(m.join(a))
print()
print(s.join(b))
print(m.join(b))

## OUTPUT:


# 1 2 3 4 5
# 1-2-3-4-5

# Aditya Kalra is broke
# Aditya-Kalra-is-broke