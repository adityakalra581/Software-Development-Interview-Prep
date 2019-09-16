#Question 3 : Find the sum of digits of number until it becomes a single digit
# numbers

# Ex:   7892

#7+9+8+2=26

#2+6=8


n=int(input("Enter the number"))
sum=0
while(True):
    q=n%10
    sum=sum+q
    r=n//10
    if r==0:
        break;
    else:
        n=r
        
        
print(sum)

# Below are the trial cases:


''' RESTART: C:/Users/aditya/Desktop/python beginning/sum of individual numbers.py 
Enter the number25

 RESTART: C:/Users/aditya/Desktop/python beginning/sum of individual numbers.py 
Enter the number25

 RESTART: C:/Users/aditya/Desktop/python beginning/sum of individual numbers.py 
Enter the number25
7
>>> 
 RESTART: C:/Users/aditya/Desktop/python beginning/sum of individual numbers.py 
Enter the number782
17
>>> 
 RESTART: C:/Users/aditya/Desktop/python beginning/sum of individual numbers.py 
Enter the number96542
26
>>> 
 RESTART: C:/Users/aditya/Desktop/python beginning/sum of individual numbers.py 
Enter the number8012354796
45'''
