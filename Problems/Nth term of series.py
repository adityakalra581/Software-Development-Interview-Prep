#Find the nth   term of the series
#0,5,26,17,124,37,342,65,728,101


# SOLUTION:
 # This is a mixed series:
 # Odd position:
     # 0 , 26 ,124 , 342, 728
#   n= 1    3   5     7    9

# Nth term= n^3-1

 # Even Position:
   # 5 ,17, 37 , 65, 101
# n= 2   4  6     8   10

# # Nth term= n^2+1


n=int(input())
if n%2==0:  #(n=even)
    p=(n**2+1)
    print(p)
else: # (n=odd)
    q=(n**3-1)
    print(q)
