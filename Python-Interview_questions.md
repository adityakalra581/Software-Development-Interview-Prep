
## Python Interview Questions 


**References**: 
- [52 most asked interview questions](https://youtu.be/YeupGcOW-3k)
- [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), 
- [Rest Api tutorial](https://www.restapitutorial.com/httpstatuscodes.html)
- [Leet code solution videos](https://www.youtube.com/@NeetCode)
- [Important Concepts](https://youtu.be/mMv6OSuitWw?si=Do2WmtzYpcGNfrpO)

1. Difference between Package and Module.

Sol : [Module vs Package Vs Library](https://techvidvan.com/tutorials/modules-vs-packages-in-python/#:~:text=A%20module%20is%20a%20file,with%20the%20locally%20extracted%20variables.)

2. What is the difference between a package and a library in Python?
```
Sol: Package is a collection of modules. It must contain an init.py file as a flag so that the python interpreter processes it as such.
     The init.py could be an empty file without causing issues. Library is a collection of packages.
```
3. What is for-else Statement.
```
Sol : [For Else in Python](https://www.w3schools.com/python/gloss_python_for_else.asp)
     Other relatable questions can be from
     1. For pass
     2. For Continue
     3. For Break
```

4. Explain Exception in python, also whether it comes in run time errors or not.
```
Sol : Unexpected event in code execution that disrupts the flow of the code.
      [Errors in Python](https://www.tutorialspoint.com/Are-Python-Exceptions-runtime-errors)
     Other useful links: [Built in exceptions in python GFG](https://www.geeksforgeeks.org/built-exceptions-python/)
```
5. Difference between Python 2 and 3.
```
Sol : [Python 2 vs Python 3](https://www.guru99.com/python-2-vs-python-3.html)
```
6. Explain decorators
7. Architecture of Django
8. What are http verbs
9. Post vs Put
10. Explain patch(http verb)
11. Explain async io in python
12. Status codes
```
Sol: HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:

- Informational responses (100–199)
- Successful responses (200–299)
- Redirection messages (300–399)
- Client error responses (400–499)
- Server error responses (500–599)
```
13. Explain Memoisation
- Memoization is a technique of recording the intermediate results so that it can be used to avoid repeated calculations and speed up the programs. It can be used to optimize the programs that use recursion. In Python, memoization can be done with the help of function decorators. 
```
# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
memory = {}
def memoize_factorial(f):
	
	# This inner function has access to memory
	# and 'f'
	def inner(num):
		if num not in memory:
			memory[num] = f(num)
			print('result saved in memory')
		else:
			print('returning result from saved memory')
		return memory[num]

	return inner
	
@memoize_factorial
def facto(num):
	if num == 1:
		return 1
	else:
		return num * facto(num-1)

print(facto(5))
print(facto(5)) # directly coming from saved memory
```
- Reference: [Memoization Decorators](https://www.geeksforgeeks.org/memoization-using-decorators-in-python/)

14. Why recursion is some cases not considered as efficient

- Recursive algorithms are often inefficient for small data, **due to the overhead of repeated function calls and returns**. For this reason efficient implementations of recursive algorithms often start with the recursive algorithm, but then switch to a different algorithm when the input becomes small.

15. Explain dynamic programming
16. What is 
```
if __name__ == "__main__":
```
```
sol: When a module is run directly this condition will hold true and when this module is imported __name__ will be equal to the name of that module.
```
- Reference: [if __name__ == "__main__":](https://youtu.be/sugvnHA7ElY)

17. Shallow vs Deep Copy:

Sol:
**Shallow Copy**:	
- Shallow Copy stores the references of objects to the original memory address.   	
- Shallow Copy reflects changes made to the new/copied object in the original object.	
- Shallow Copy stores the copy of the original object and points the references to the objects.	
- Shallow copy is faster.

**Deep Copy**:
- Deep copy stores copies of the object’s value.
- Deep copy doesn’t reflect changes made to the new/copied object in the original object.
- Deep copy stores the copy of the original object and recursively copies the objects as well.
- Deep copy is comparatively slower.



Reference: 
1. [Shallow vs Deep Copy Krish Naik](https://youtu.be/SgUwPDT9tEs)
2. [GFG Article](https://www.geeksforgeeks.org/difference-between-shallow-and-deep-copy-of-a-class/)
```
## Only = 

lst1 = [1,2,3]
lst2 = lst1

## Before change
print(lst2)
## [1, 2, 3]

lst1[0] = 100

## After change
print(lst2)
## [100, 2, 3]

# --------------------------------------------

## Shallow Copy: If we have 1d list the changes in one list won't change the other, but 2d list will be altered with alteration in the original list


lst1 = [1,2,3]
lst2 = lst1.copy()

## Before change
print(lst2)
## [1, 2, 3]

lst1[0] = 100

## After change
print(lst2)
## [1, 2, 3]
## There is no change in second list

## Let's try another use case:

temp1 = [[1,2,3],[4,5,6]]
temp2 = temp1.copy()

print("before altering element: ",temp2)

temp1[1][0] = 1000
print("After altering element List 1: ",temp1)
print("After altering element List 2: ",temp2)

# --------------------------------------
## Output: 
# before altering element:  [[1, 2, 3], [4, 5, 6]]
# After altering element List 1:  [[1, 2, 3], [1000, 5, 6]]
# After altering element List 2:  [[1, 2, 3], [1000, 5, 6]]

# ---------------------------------------------------------------------------

## Deep Copy: The copied list will never be altered with alterations in original list.

import copy

lst1 = [1,2,3]
lst2 = copy.deepcopy(lst1)

## Before change
print(lst2)
## [1, 2, 3]

lst1[0] = 100

## After change
print(lst2)
## [1, 2, 3]
## There is no change in second list

## Let's try another use case:

temp1 = [[1,2,3],[4,5,6]]
temp2 = copy.deepcopy(temp1)

print("before altering element: ",temp2)

temp1[1][0] = 1000
print("DeepCopy After altering element List 1: ",temp1)
print("DeepCopy After altering element List 2: ",temp2)

## Output:

# before altering element:  [[1, 2, 3], [4, 5, 6]]
# DeepCopy After altering element List 1:  [[1, 2, 3], [1000, 5, 6]]
# DeepCopy After altering element List 2:  [[1, 2, 3], [4, 5, 6]]



```

<!-- -------------------------------------- -->

### Core Python Interview Questions

1. How do we write codes in python?
2. What is ‘suite’?
3. What are the different data types in python?
4. What are different ways to concatenate a tuple?
5. What is a slice operator?
6. What are the different types of functions in python?
7. Can you define a class in python? How will you write a code and it’s method for an Employee class?
Create a method to print and call an object for this class.
8. What is init and self keywords in python?
9. What is pass statement?
10. How can you get a first digit of a string?
11. Regular expressions?
12. Which class do we use for ‘regular expression’ in python?
13. Explain string.capitalize() in python
14. File handling [Reading, peeking on top, open in different modes]
15. Ordered vs Unordered data structures in python.

- Ordered means that the data structure retains the ordering as provided by the programmer; Python examples of ordered structures are strings, lists, and tuples. The ordering being discussed here is the result of iterating around the structure in a for loop.

- Non ordered means that the data structure doesn’t have a specific order, and doesn’t care about any ordering by the programmer. In Python a set is non-ordered, and a dictionary is mostly non-ordered (it preserves the order in which the keys are added, but a programmer cannot insert something as the 3rd item into a dictionary).

<!-- ------------------------------------------------ -->

### [Django Interview Questions InterviewBit](https://www.interviewbit.com/django-interview-questions/)

### [Django interview Question Video Tutorial](https://youtu.be/9ai0b1LRMQM)


1. How comfortable are you with Python?
2. HTML/CSS Skill level?
3. Any JavaScript Experience?
4. What is Django?
5. What can you build with Django?
- (https://www.netguru.com/blog/django-apps-examples)
6. Difference Between a Project & App?
- Entire website can be considered as project and apps are small component of a project. For ex. Facebook.com is a project and news feed can be an app for it in django terms
7. How do we initialize a project?
8. How do we initialize an app?
9. How do we start our development server?
```
django-admin startproject <project_name>
python manage.py startapp
python manage.py runserver
```
10. What does the settings.py file do?
11. What are models? What are views? What are templates?
12. What are url patterns?
13. What is the Django Admin panel?
14. Make migrations & migrate command
15. FBV vs CBV
16. What database system do you prefer?
17. How do you set up a database connection?
18. Why do we add names to URL's & how do we access them dynamically?
19. Where do we store templates?
20. Django Templating Language
21. What are static files?

<!-- ---------------------------------------------------------- -->
22. Serving static files during development?
23. What is MEDIA_ROOT
24. What does "python manage.py collectstatic" do?
25. Serving static files during production?
26. Common Model attributes
27. Querying the database
28. What are CSRF Tokens?
29. What are Model Forms?
30. What is DRF?
31. What are Django Signals?
32. How can we set restrictions on views?
33. What are Model Serializers?

### Numpy and Pandas Interview Questions

- References:
1. [Pandas Documentation](https://pandas.pydata.org/docs/getting_started/install.html)

1. How to add two dataframes
```
sol: 
1. merge
2. Concat
3. append
4. join
```
2. Does Pandas support SQL Queries
3. Merging two dataframes on a single column

sol: pandas.merge command [side by side merging]

- Reference:
1. [Pandas merge docs](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html)
2. [Pandas merge](https://youtu.be/h4hOPGo4UVU)

