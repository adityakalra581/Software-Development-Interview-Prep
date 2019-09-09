a=int(input("Enter the greater number :"))
b=int(input("enter the second number :"))
if a>b:
    c=a
else:
    c=b


#while True means loop forever. The while statement takes an
#expression and executes the loop body while the expression
#evaluates to (boolean) "true".
#True always evaluates to boolean "true" and thus executes the loop body
#indefinitely. 


while(True):
    if (c%a==0)and(c%b==0):
        LCM=c
        break;
    c = c+1 



    
print("The LCM of the two numbers are: ",LCM) 


# logic of lcm:
# that number which is completely divisible by both the numbers that
# is an lcm.

# for eg: 25 & 15 can completely divide 75,150.....
# so here lcm is 75(least common multiple)
