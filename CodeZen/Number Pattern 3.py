n=int(input())
print('1')
print('11')
x='2'
l=[]
for i in range(3,n+1):
    l.append(1)
    l.append((i-2)*x)
    l.append(1)
    print(*l,sep='')
    l=[]
