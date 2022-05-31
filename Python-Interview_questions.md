1. Difference between Package and Module.

Sol : [Module vs Package Vs Library](https://techvidvan.com/tutorials/modules-vs-packages-in-python/#:~:text=A%20module%20is%20a%20file,with%20the%20locally%20extracted%20variables.)

2. What is the difference between a package and a library in Python?
Sol: Package is a collection of modules. It must contain an init.py file as a flag so that the python interpreter processes it as such.
     The init.py could be an empty file without causing issues. Library is a collection of packages.

3. What is for-else Statement.

Sol : [For Else in Python](https://www.w3schools.com/python/gloss_python_for_else.asp)
     Other relatable questions can be from
     1. For pass
     2. For Continue
     3. For Break


4. Explain Exception in python, also whether it comes in run time errors or not.

Sol : Unexpected event in code execution that disrupts the flow of the code.
      [Errors in Python](https://www.tutorialspoint.com/Are-Python-Exceptions-runtime-errors)
     Other useful links: [Built in exceptions in python GFG](https://www.geeksforgeeks.org/built-exceptions-python/)

5. Difference between Python 2 and 3.

Sol : [Python 2 vs Python 3](https://www.guru99.com/python-2-vs-python-3.html)

6. Explain decorators
7. Architecture of Django
8. What are http verbs
9. Post vs Put
10. Explain patch(http verb)
11. Explain async io in python
12. Status codes

Sol: [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), 
[Rest Api tutorial](https://www.restapitutorial.com/httpstatuscodes.html)

13. Explain Memoisation
14. Why recursion is some cases not considered as efficient
15. Explain dynamic programming

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

<!-- ------------------------------------------------ -->

### [Django Interview Questions InterviewBit](https://www.interviewbit.com/django-interview-questions/)

### [Django interview Question Video Tutorial](https://youtu.be/9ai0b1LRMQM)


1. How comfortable are you with Python?
2. HTML/CSS Skill level?
3. Any JavaScript Experience?
4. What is Django?
5. What can you build with Django?
6. Difference Between a Project & App?
7. How do we initialize a project?
8. How do we initialize an app?
9. How do we start our development server?
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

<!-- ------------------------------------------------------------ -->

### TCS Technical Interview 14th and 16th May 2022

**- Django**

1. Architecture of Django
2. Database connection in Django. Difference between MVC and MVT architecture
3. What is ORM and have you used it, if yes How?

**- SQL**

4. Maximum value of a column in a table
5. Top 5 values of a column

**- Python**

6. WAP which output a dictionary in which keys are length of a given integer in a list and it's values are that length values in a list

```
Input:
temp = [1,2,100,200,30]

output = {}
## {1: [1,2]; 3:[100,200]; 2:[30]}

# Key: length of int
# Value: length matches the key it should be in list
```
```
Solution:

for i in temp:
    length = len(str(i))
    if length in output.keys():
        output[length].append(i)
    else:
        output[length] = [i]

print(output)
```
7. What are APIs
8. Difference between PUT and POST methods
9. What is Filter, Map and Reduce
10. How to open a file in python
11. Explain **with** keyword
12. Give few example of the math functions
13. Explain and give examples of short hand operators
14. Is python dynamically typed language
15. Is numpy series a linear data structure.
16. List vs numpy array?

<!-- ------------------------------------------------------------ -->

### Sunday Labs Technical Interview 27th May 2022

1. Second highest salary in a column (SQL)

```
select max(salary) from employee where salary<(select max(salary) from emp);
or
select *from employee group by salary order by  salary desc limit 1,1;
```
solution: [second highest salary article](https://www.geeksforgeeks.org/sql-query-to-find-second-largest-salary/)

2. What is PIP in python
3. Set vs tuples difference
4. What are immutable data structures
5. Difference between the latest python version and versions before that
6. Coding Question: Reverse the sentence

```
new = "my name is aditya"
temp = new.split()[::-1]
print("Reversed list: ",temp)
output = []

for i in temp:
    output.append(i)

print("final result:", " ".join(output))
```