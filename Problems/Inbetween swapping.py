
## Swapping the elements right which are completely divisible by 7.
## Swapping should be only one place right in the list.
## for eg.

# original list= [1,3,7,8,14,76,21,9]
# after swapping = [1,3,8,7,76,14,9,21]



l=[1,2,3,7,9,14,5,21,0]
i=0
n=len(l)

while i<n:
    if l[i]%7==0:
        l[i],l[i+1]=l[i+1],l[i]
        i=i+2
    else:
        i=i+1
        
print(l)


#  l[i],l[i+1]=l[i+1],l[i] this statement might not work in software
# older than python3.7
