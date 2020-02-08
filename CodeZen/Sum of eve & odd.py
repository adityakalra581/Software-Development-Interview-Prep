## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
l=list(map(int,input().rstrip()))
even=0
odd=0
#print(l)
for i in l:
    if i%2==0:
        even+=i
    else:
        odd+=i
print(even," ",odd)
        

