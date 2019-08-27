# Getting input of two tuples and swapping them.



t=tuple()
u=tuple()


n=int(input("Enter the length of tuple 1:"))
m=int(input("Enter the length of tuple 2:"))

for i in range(n):
    a = input("Enter the Element for tuple 1:")
    t +=  (a,)


for j in range(m):
    b = input("Enter the Element for tuple 2:")
    u += (b,)

print("The original tuple t is:",t)
print("The original tuple u is:",u)

print("____________________________")
## For swapping

t,u=u,t
print("tuple 1 after swapping:",t)

print("tuple 2 after swapping:",u)

        
