

## BOTH THE METHODS ARE WORKING PERFECTLY.



n=int(input())
print("1")
print("11")
x='0'
l=[]
#print(3*x)
for i in range(2,n+1):
    print(i,end='')
    print((i-1)*x,end='')
    print(i)

    

'''
n=int(input())
print("1")
print("11")
x='0'
l=[]
if n>2:
    for i in range(3,n+1):
        # print(i,((i-1)*x),i)  is not working.
        # Need to find out how to print without spaces.
        l.append(i-1)
        l.append((i-2)*x)
        l.append(i-1)
        print(*l,sep='')   # .join() not worked here as it is for strings.
        l=[]               # We can use *list,sep='anything' 
'''
