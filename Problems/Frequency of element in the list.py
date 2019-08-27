## WAP To display the frequencies of all the elements in the list.

lst=[12,45,45,67,33,45,89,90,89,78,34]
print(lst)
l=[]
m=[]

n=len(lst)

for i in lst:
    if i not in l:
        # This will provide original values in l
        x=lst.count(i)
        l.append(i)

        # All the frequencies will be stored inside m.
        m.append(x)   
        
    

print("Elements",'\t\t','Frequency')
for j in range(len(m)):

    # Length of m and l are same so we can take both.
    
    print(l[j],'\t\t\t\t',m[j])
    # The above command will print value of l[j] and then m[j].

