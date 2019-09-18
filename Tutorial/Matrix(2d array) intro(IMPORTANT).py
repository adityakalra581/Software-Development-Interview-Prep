# A basic code for matrix input from user



# For small Inbalanced Matrix Use This CODE:
# Where Rows != Columns

'''R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 

# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 

# For user input 
for i in range(R):		 # A for loop for row entries 
	a =[] 
	for j in range(C):	 # A for loop for column entries 
		a.append(int(input())) 
	matrix.append(a) 

# For printing the matrix 
for i in range(R): 
	for j in range(C): 
		print(matrix[i][j], end = " ") 
	print() '''
    


# For All other Balanced Matrix use this:(More Efficient and Neat)
m=[]

for _ in range(3):
        m.append(list(map(int,input().rstrip().split())))
        # EXPLANATION:
        # a list is appended in m, as m is a 2d array.
        # map is used here as list does not take more than one argument.
        # int, input() = for integer input.(do not use int for string input)
        # rstrip = idk yet.
        # .split() = After every input a space is required for the next input to be admissible.
        
print(m)        
# For Matrix View:

print('\n'.join([''.join(['{:4}'.format(items) for items in rows])
                for rows in m ]))
# EXPLANATION:
# '\n' : new line
# 1st .join() has "([''.join(['{:4}'.format(items) for items in rows])for rows in m ])" this as argument.

# 2nd .Join() has   "(['{:4}'.format(items) for items in rows])" has this in argument. 

# There are 2 join(),2 items, 2 rows
# there is 1 m(matrix to be presented, 1 .format() and 1{:4}









