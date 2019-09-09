a=int(input("Enter the greater number"))
b=int(input("enter the second number"))
l=[] # Has the factors of a
m=[] # Has the factors of b
c=[] # common factors of a and b


# The idea of HCF is Highest Common Factor
# So in this code list c maximum value will be the HCF of two numbers

for i in range(2,a+1):
    if a%i==0:
        l.append(i)
        
        
        
for j in range(2,b+1):
    if b%j==0:
        m.append(j)        

        
print(l)        

print(m)

for h in l:
    if h in m:
        c.append(h)
#return (list(set(li1) - set(li2))) 


        
print(c)
print("The HIGHEST COMMON FACTOR IS :",max(c))
