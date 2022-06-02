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

## ZENARATE Technical interview may 31st


1. Diamond Problem 
Sol: Multiple inheritance problem, as java doesn't support multiple inheritance.

2. Multiple Inheritance support ?
Sol: In python we can inherit multiple times unlike java so the diamond problem doesn't occur in python.

3. Interface, need?
4. Types of polymorphism?
5. Late static binding
6. Multipart request
7. Microservice vs Monolithic Architecture

sol: A monolithic architecture is the traditional unified model for the design of a software program. Monolithic, in this context, means **composed all in one piece.** According to the Cambridge dictionary, the adjective monolithic also means both **too large** and **unable to be changed.**

8. REST[Representational state transfer] vs SOAP[Simple object access protocol]

Sol: Many legacy systems may still adhere to SOAP, while REST came later and is often viewed as a faster alternative in web-based scenarios. REST is a set of guidelines that offers flexible implementation, whereas SOAP is a protocol with specific requirements like XML messaging.

REST APIs are lightweight, making them ideal for newer contexts like the Internet of Things (IoT), mobile application development, and serverless computing. SOAP web services offer built-in security and transaction compliance that align with many enterprise needs, but that also makes them heavier. Additionally, many public APIs, like the Google Maps API, follow the REST guidelines.

-Reference: [Rest vs soap](https://www.redhat.com/en/topics/integration/whats-the-difference-between-soap-rest)

9. Multiple Jquery versions on same page ?
10. Check if string is palindrom

```
newString = “aditya”
temp=newString[::-1]
If newString == temp:
```	

11. Find out all the occurences of substring. Limit of characters in substring is 2.[Ignore case]

```
String_original = “asdhakafhAditaksdakAdityadas”
Substring = “Aditya”
```
			

12. Middle element of linked list
13. BFS vs DFS ( shortest path )

14. Problem: You need to delete the rows with the duplicate names from the table Person

```
Table Person
ID	Name		Gender
1	A		male
2	B		male
3	A		female
4	D		female
5	E		male
… 
…

To find duplicate values:
SELECT NAME, COUNT(NAME) FROM PERSON GROUP BY NAME HAVING COUNT(NAME) > 1

WITH EmployeesCTE AS
(
   SELECT *, ROW_NUMBER() OVER (PARTITION BY ID ORDER BY ID) AS RowNumber
   FROM Employees
)
DELETE FROM EmployeesCTE WHERE RowNumber > 1

```
[Deleting duplicate records](https://youtu.be/ynWgSZBoUkU)



15. Problem: Every record in the table Person is having incorrect gender, you have to write an update query to fix all the records.
Expected Result:
Table Person
ID	Name		Gender
1	A		female
2	B		female
3	A		male
4	D		male
5	E		female

UPDATE PERSON
SET GENDER = “FEMALE”
WHERE GENDER =”F”


UPDATE PERSON
SET GENDER = “MALE”
WHERE GENDER =”FEMALE”

UPDATE PERSON
SET GENDER = “F”
WHERE GENDER =”MALE”

16. Storage engine in MYSQL
17. Drawback of auto-increment columns
18. Table level locking vs row level locking
19. Max number of triggers on a table, usecase	
20. Stored procedure vs functions
21. Authentication vs Authorization

Sol: Simply put, authentication is the process of verifying who someone is, whereas authorization is the process of verifying what specific applications, files, and data a user has access to.
[Authentication vs Authorization](https://www.sailpoint.com/identity-library/difference-between-authentication-and-authorization/)

22. Oauth2.0 ( basic, bearer token)

23. Shallow vs deep copy **[Asked twice atleast]**
- [Shallow vs Deep copy](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/)

24. Decorators **[Asked multiple times]**

Sol: A decorator in Python is a function that takes another function as its argument, and returns yet another function . 
- [Decorators in python](https://www.geeksforgeeks.org/decorators-in-python/)
- [Decorators video tutorial](https://youtu.be/FsAPt_9Bf3U)

25. GET(200), PUT(204), POST(201) and their success codes

Sol: HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:

- Informational responses (100–199)
- Successful responses (200–299)
- Redirection messages (300–399)
- Client error responses (400–499)
- Server error responses (500–599)

- References: [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), 
[Rest Api tutorial](https://www.restapitutorial.com/httpstatuscodes.html)

26. What is a view

Sol: In SQL, a view is a virtual table based on the result-set of an SQL statement. A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database. You can add SQL statements and functions to a view and present the data as if the data were coming from one single table.

- [View in SQL](https://www.w3schools.com/sql/sql_view.asp)

## Deloitte Technical Interview (AWS-Python profile) 1st June 2022

1. Flask vs Django
2. urls in flask or routing in flask
3. Services of AWS you have used
4. AWS Lambda
5. Directories or file structure django vs flask projects
6. How to better the time to fetch results in sql if the query is already optimized. (Partition or indexing or any other solution)