'''

Sample Input :
7
Sample Output :
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG

'''

## Important:

# chr(65) ='A'
# chr(97) ='a' 




n=int(input())
x=64
for i in range(1,n+1):
    for j in range(i):
        print(chr(x+i),end='')
    print()
