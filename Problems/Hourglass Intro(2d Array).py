# HourGlass Intro

a = [[0, -4, -6, 0, -7, -6,],
[-1, -2, -6, -8, -3, -1],
[-8, -4, -2, -8, -8, -6],
[-3, -1, -2, -5, -7, -4],
[-3, -5, -3, -6, -6, -6],
[-3, -6, 0, -8, -6, -7]]

#print(a)

#print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
 #     for row in A]))

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in a]))


#numrows = len(input)    
#numcols = len(input[0])

R= len(a) # This will give rows
C= len(a[0]) # This will give Columns.
print(R)
print(C)

h=[]
H=[]
#sum_1 = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
#list_sum.append(sum_1)
for i in range(R-2):
    for j in range(C-2):
        h=[a[i][j],a[i][j+1],a[i][j+2],a[i+1][j+1],a[i+2][j],a[i+2][j+1],a[i+2][j+2]]
        H.append(h)
        

#print(H)
print("The hourglass is not in it's original format but presented Row wise")
print("That means every row is an Hourglass")
print("All the posibilities of HourGlass are: ",'\n','\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in H]))

print("The Total Hourglass are: ",len(H))


