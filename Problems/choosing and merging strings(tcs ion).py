#4. Accept 2 strings ,all letters at odd position of string 1
#followed  by all letters at even position at string2 should form a
#third string then merge all the three strings and display

# Ex: India(Ida)

# Pakisthan (aita)

# Third string should be Idaaita

# Final result is IndiaPakisthanIdaaita




a=input("Enter the First String : ")
b=input("Enter the second String : ")
n=len(a)
m=len(b)
c=[]
for i in range(n):
    if i%2==0:
        c.append(a[i])
for j in range(m):
    if j%2!=0:
        c.append(b[j])   
#IMP: join(list) only works with string type list
# so if the list was integer type you would have to convert it into a string.
R=(''.join(c))
print(R)
print(a+b+R)
print()
print('***************************************')
print()
# List Comprehension Approach (Efficient Code)
# 4 lines less and neat approach.
'''a=input("Enter the First String : ")
b=input("Enter the second String : ")
n=len(a)
m=len(b)
c=[a[i] for i in range(n) if i%2==0 ]
d=[b[j] for j in range(m) if j%2!=0 ]
J=(''.join(d))
R=(''.join(c))
print(R+J)
print(a+b+R+J)'''

# OUTPUT:

"""Enter the First String : INDIA
Enter the second String : PAKISTHAN
IDAAITA
INDIAPAKISTHANIDAAITA

***************************************"""





