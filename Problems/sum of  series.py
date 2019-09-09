#18. WAP to find the sum of the given series till n terms
#1+(1+2)+(1+2+3)+…+(1+2+3+…+n)





n=int(input())
sum1=0
a=[]
for i in range(1,n+1):
    sum1=sum1+i
    a.append(sum1)
#print(sum1)
print(a)
print("The Sum Of the Series is: ",sum(a))
