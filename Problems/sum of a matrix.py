a=[[1,2,3],[4,5,6],[4,2,7]]
b=[[2,2,2],[4,3,2],[8,8,8]]

c=[[0,0,0],[0,0,0],[0,0,0]]

print(len(a))
# len(a) is basically no. of rows

# len(a[0]) is no. of columns.

# Imp. len(a)=len(b)
#      len(a[0]) =len(b[0]) for addition to take place.


print(len(a[0]))

for i in range(len(a)):
# The above loop will run 3 times in this case
# for i = 0,1,2
    
    for j in range(len(a[0])):
# the above loop is for columns and it will run 9 times.
# for i =o ,j will be =0,1,2
#  for i =1 ,j will be =0,1,2
#  for i =2 ,j will be =0,1,2
# so 9 times.
        
        c[i][j]=a[i][j]+b[i][j]

print(c)
