<!-- ------------------------------------------------------------ -->

### Companies I Interviewed for [Python Developer or related profile]

1. Coding Ninjas - Failed
2. Deloitte - Failed
3. Bold - Failed
4. Zenarate - Failed
5. Sunday Labs - Failed
6. Octros - Failed
7. TCS - Cleared
8. Capgemini - Cleared
9. Gemini Solutions - Cleared
10. Tetaras Data - Cleared


### Coding Ninjas Jan 2022
**[FAILED SECOND ROUND]**

- Q.1 Finding second highest element in an array.

- Q.2 Finding duplicates in an array and probably their count.

- Q.3 Time complexities of many algorithms and Data structure operations

- Q.4 HTTP verbs

```
- Get,Post,Put,Delete (Main ones), others: Head,connect,options,trade,patch
- (https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

- Follow up question: diff. between put and patch?
- (https://www.geeksforgeeks.org/difference-between-put-and-patch-request/)
```

### Expedia SDE 2 Hackerrank Test 8th March 2022
**[CLEARED]**
Coding Test on HackerRank

- Q.1 Device Name System: 

```
The aim is to create unique device names. If a device already exists with a similar name, append an integer incremented by 1 for each occurrence.

Input: ['lamp', 'lamp', 'tv', 'lamp']

Expected Output: ['lamp', 'lamp1', 'tv', 'lamp2']
```

Reference: https://stackoverflow.com/questions/62929107/creating-unique-device-names


- Q.2 Math Homework
Reference: https://leetcode.com/discuss/interview-question/799301/students-have-been-assigned-a-series-of-math-problems

- Q.3 Number of Moves
Reference: https://leetcode.com/discuss/interview-question/865012/number-of-moves-chessboard-online-assessment-hackerrank

### TCS Technical Interview 14th and 16th May 2022
**[CLEARED]**

**- Django**

1. Architecture of Django
```
Django is based on MVT (Model-View-Template) architecture. MVT is a software design pattern for developing a web application.
(https://www.geeksforgeeks.org/django-project-mvt-structure/)
```
2. Database connection in Django. Difference between MVC and MVT architecture

```
DB connection in django: Adding DATABASES in settings.py. Django officially supports the following databases: PostgreSQL. MariaDB. MySQL.
Default is sqlite3
Reference: https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/
--------------------------------------------------------------------------------
MVC: Model(DB connection,queries) View(UI) Controller(Business logic)
Tech using MVC: Ruby on Rails, Spring MVC,Java Servlet,Laravel, Express, and Angular

MVT: Model(DB connection,queries) View(Business logic) Template(UI)
------------------------------------------------------------------------------
Reference: https://youtu.be/HnbDM1fIkng?si=FL4l0M_dAayIna_6
```

3. What is ORM and have you used it, if yes How?
```
Django ORM (Object-Relational Mapping) module is a feature of the Django web framework that enables developers to interact with databases using high-level object-oriented APIs instead of writing SQL queries directly.
```
**- SQL**

4. Maximum value of a column in a table
5. Top 5 values of a column

```
select * from table where column = (select max(column) from table);
select * from table order by column desc limit 5;
```

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
7. What are APIs (Application programming interface)
8. Difference between PUT and POST methods
9. What is Filter, Map and Reduce

Sol: reduce() works differently than map() and filter() . It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value. Also, in Python 3 reduce() isn't a built-in function anymore, and it can be found in the functools module.
Reference: [Filter, Map and Reduce](https://www.analyticsvidhya.com/blog/2021/07/python-most-powerful-functions-map-filter-and-reduce-in-5-minutes/)

10. How to open a file in python
```
(https://www.geeksforgeeks.org/file-handling-python/)
```
11. Explain **with** keyword
```
(https://www.geeksforgeeks.org/with-statement-in-python/)
```
12. Give few example of the math functions
```
(https://www.w3schools.com/python/module_math.asp)
```
13. Explain and give examples of short hand operators
14. Is python dynamically typed language?
```
Dynamically typed languages
Perform type checking at runtime, while the code is being executed. This means that dynamically typed languages can compile even if they contain errors that will prevent the script from running properly. Examples of dynamically typed languages include Python, Ruby, and JavaScript.
Statically typed languages
Perform type checking at compile time, before the code is executed. This means that statically typed languages will fail to compile until the errors have been fixed. Examples of statically typed languages include Java, C++, and C#. 

```
15. Is numpy series a linear data structure.
16. List vs numpy array?

<!-- ------------------------------------------------------------ -->

### Sunday Labs Technical Interview 27th May 2022 
**[FAILED]**

1. Second highest salary in a column (SQL)

```
select max(salary) from employee where salary<(select max(salary) from emp);
or
select *from employee group by salary order by  salary desc limit 1,1;
```
solution: [second highest salary article](https://www.geeksforgeeks.org/sql-query-to-find-second-largest-salary/)

2. What is PIP(Preferred Installer Program) in python
```
Pip is a package manager for Python that makes it easier to install and manage third-party libraries. It allows you to download and manage Python packages from the Python Package Index (PyPI) or other package repositories. For example, you can use the command pip install package_name to install packages.
```
3. Set vs tuples difference
4. What are immutable data structures
5. Difference between the latest python version and versions before that
6. Coding Question: Reverse the sentence

```
## Reverse a sentence
## Input: "my name is aditya"
## Required output: aditya is name my

new = "my name is aditya"
temp = " ".join(new.split()[::-1]) 
print("Reversed list: ",temp)
## .split() will split each word, [::-1]: reverse order, " ".join(): join list every element with a space
## temp will be a list before join, after join becomes a string.
```

### ZENARATE Technical interview may 31st
**[FAILED]**


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

- Reference: [Rest vs soap](https://www.redhat.com/en/topics/integration/whats-the-difference-between-soap-rest)

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

Expected Output: ['adit','aditya']
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
```
Expected Result:
Table Person
ID	Name		Gender
1	A		female
2	B		female
3	A		male
4	D		male
5	E		female

UPDATE Person
SET gender = CASE WHEN gender = 'male' THEN 'female' 
                  WHEN gender = 'female' THEN 'male' END
WHERE gender IN ('male','female')
```

16. Storage engine in MYSQL.
sol: 
- List of storage engines
MySQL supported storage engines:

1. InnoDB
2. MyISAM
3. Memory
4. CSV
5. Merge
6. Archive
7. Federated
8. Blackhole

- **InnoDB** is the most widely used storage engine with transaction support. It is an ACID compliant storage engine. **It supports row-level locking, crash recovery and multi-version concurrency control**. It is the only engine which provides foreign key referential integrity constraint. Oracle recommends using InnoDB for tables except for specialized use cases.

- **MyISAM** is the original storage engine. It is a fast storage engine. It does not support transactions. **MyISAM provides table-level locking**. It is used mostly in Web and data warehousing.

- Reference: [Storage Engines in MySQL](https://zetcode.com/mysql/storageengines/)

17. Drawback of auto-increment columns
18. Table level locking vs row level locking
19. Max number of triggers on a table, usecase	
20. Stored procedure vs functions
21. Authentication vs Authorization

Sol: Simply put, authentication is the process of verifying who someone is, whereas authorization is the process of verifying what specific applications, files, and data a user has access to.
[Authentication vs Authorization](https://www.sailpoint.com/identity-library/difference-between-authentication-and-authorization/)

22. Oauth2.0 ( basic, bearer token)
sol: 
OAuth 2.0, which stands for “Open Authorization”, is a standard designed to allow a website or application to access resources hosted by other web apps on behalf of a user. It replaced OAuth 1.0 in 2012 and is now the de facto industry standard for online authorization.

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

### Deloitte Technical Interview (AWS-Python profile) 1st June 2022

- **First round** [Cleared]

1. Flask vs Django
```
What is Django?
Django is an open-source full-stack web framework written in Python that follows the MVT (model-view-template) architectural pattern and a DRY principle (Don’t Repeat Yourself). It was made by Adrian Holovaty and Simon Willison and was publicly published in 2005. The name given is based on the singer Django Reinhardt. It is a great choice who want to build web applications that are secure, scalable, flexible, and easy to maintain

What is Flask?
Flask is an open-source beginner-friendly micro-web framework written in Python that follows the MVC (model-view-controller) architectural pattern and supports Jinja templates, which can be used to create views. It was made by Armin Ronacher of Pocoo, an international group of Python enthusiasts formed in 2004. The name “Flask” is a reference to the earlier Bottle framework. It is a great choice to build small to medium level web application and where performance is not much of a issue and developer need flexibility.


What is FastAPI?
FastAPI is also an open-source Starlette-ASGI (Asynchronous Server Gateway Interface) micro-web framework written in Python used to create RESTful APIs. It was made by Sebastián Ramírez in December 2018. The name is based on the speed to develop API hence ‘FastAPI’. It is a great choice for building fast performance APIs and microservices
- (https://www.geeksforgeeks.org/comparison-of-fastapi-with-django-and-flask/)
```

2. urls in flask or routing in flask
```
Using @app.route for examples:
@app.route("/login")
def login():
    return render_template('login.html')

## Add a login:
@app.route('/login',methods=['POST'])
def add_login():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']
    password = request.json['password']
    
    new_login = Login(name,email,phone,password)

    db.session.add(new_login)
    db.session.commit()

    return login_schema.jsonify(new_login)



## All logins
@app.route('/login',methods=['GET'])
def get_logins():
    all_logins = Login.query.all()
    result = logins_schema.dump(all_logins)
    return jsonify(result)


(https://www.youtube.com/watch?v=XTLg6TLfy7M)
```
3. Services of AWS you have used
4. AWS Lambda
5. Directories or file structure django vs flask projects
6. How to better the time to fetch results in sql if the query is already optimized. (Partition or indexing or any other solution)

- **Second Round** [Mostly AWS] [Failed] 

1. What is AMI
- Sol: An Amazon Machine Image (AMI) is a supported and maintained image provided by AWS that provides the information required to launch an instance. You must specify an AMI when you launch an instance. You can launch multiple instances from a single AMI when you require multiple instances with the same configuration. You can use different AMIs to launch instances when you require instances with different configurations.

Reference: [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

2. What is AWS lambda
```
AWS Lambda, or Amazon Web Services Lambda, is a serverless computing cloud service that allows developers to run code in response to events without managing servers. It's sometimes called function-as-a-service (FaaS).
You can use AWS Lambda to run code without provisioning or managing servers.
Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, and logging. With Lambda, all you need to do is supply your code in one of the language runtimes that Lambda supports.
You organize your code into Lambda functions. The Lambda service runs your function only when needed and scales automatically. You only pay for the compute time that you consume—there is no charge when your code is not running.

Lambda is an ideal compute service for application scenarios that need to scale up rapidly, and scale down to zero when not in demand. For example, you can use Lambda for:
File processing: Use Amazon Simple Storage Service (Amazon S3) to trigger Lambda data processing in real time after an upload. 

References:
(https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
(https://www.interviewbit.com/aws-lambda-interview-questions/)
```

3. What do you understand by Serverless
```
Serverless computing in Amazon Web Services (AWS) allows developers to build and run applications and services without managing servers. Instead, AWS manages the underlying infrastructure, including provisioning, scaling, and maintenance. This allows developers to focus on their application code, while still receiving the benefits of cost-effective, efficient, and scalable server infrastructure. 

```

4. EC2 vs Lambda
```
EC2
A virtual cloud infrastructure service that offers resizable compute capacity in the cloud. It's a traditional compute solution that can be used for high-performance computing, disaster recovery, and DevOps processes.
Serverless
An execution model where the cloud provider dynamically allocates resources to execute code. Serverless computing services can be cost-efficient, scalable, and provide built-in availability and fault tolerance.

The choice between EC2 and a serverless service depends on your use case and requirements. For example, AWS Lambda is a serverless service that can be used for applications that run on-demand in 15 minutes or less, or when you want to pay only for the capacity you use.
```

5. Use cases of lambda function
```
When to use Lambda

Lambda is an ideal compute service for application scenarios that need to scale up rapidly, and scale down to zero when not in demand. For example, you can use Lambda for:
File processing: Use Amazon Simple Storage Service (Amazon S3) to trigger Lambda data processing in real time after an upload.
Stream processing: Use Lambda and Amazon Kinesis to process real-time streaming data for application activity tracking, transaction order processing, clickstream analysis, data cleansing, log filtering, indexing, social media analysis, Internet of Things (IoT) device data telemetry, and metering.
Web applications: Combine Lambda with other AWS services to build powerful web applications that automatically scale up and down and run in a highly available configuration across multiple data centers.
IoT backends: Build serverless backends using Lambda to handle web, mobile, IoT, and third-party API requests.
Mobile backends: Build backends using Lambda and Amazon API Gateway to authenticate and process API requests. Use AWS Amplify to easily integrate with your iOS, Android, Web, and React Native frontends.

When using Lambda, you are responsible only for your code. Lambda manages the compute fleet that offers a balance of memory, CPU, network, and other resources to run your code. Because Lambda manages these resources, you cannot log in to compute instances or customize the operating system on provided runtimes. Lambda performs operational and administrative activities on your behalf, including managing capacity, monitoring, and logging your Lambda functions.
```

6. What is lambda layer
```
A Lambda layer is a .zip file archive that contains supplementary code or data. Layers usually contain library dependencies, a custom runtime, or configuration files.

There are multiple reasons why you might consider using layers:
To reduce the size of your deployment packages. Instead of including all of your function dependencies along with your function code in your deployment package, put them in a layer. This keeps deployment packages small and organized.
To separate core function logic from dependencies. With layers, you can update your function dependencies independent of your function code, and vice versa. This promotes separation of concerns and helps you focus on your function logic.
To share dependencies across multiple functions. After you create a layer, you can apply it to any number of functions in your account. Without layers, you need to include the same dependencies in each individual deployment package.
To use the Lambda console code editor. The code editor is a useful tool for testing minor function code updates quickly. However, you can’t use the editor if your deployment package size is too large. Using layers reduces your package size and can unlock usage of the code editor.


```

- References:
- [AWS Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html#:~:text=A%20Lambda%20layer%20is%20a,size%20of%20your%20deployment%20packages)
- [Video tutorial](https://youtu.be/stovPJCVXcw)

7. Extra storage in EC2

8. What tier do you use for s3 bucket

and a lot about EC2 ..................

9. Modules you have used in python.

10. What kind of CI/CD pipeline you use.

sol: Jenkins we use, other tools are azure pipelines and github actions.

11. Rank vs Dense Rank   

### Bold Interview 1st Round 9th June
**[Failed]**

1. Return vs Yield keyword
2. Can we declare a variable using self in one of the functions of a class

```
class A:
    some code
    ...

    def B:
        self.some_variable

```

can we do this?

3. Shallow vs Deep Copy

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

- What are the Consequences of Using Shallow Copy on Mutable Objects?
Shared References: Changes to mutable nested objects in the copied object will affect the original object and vice versa. This is because the nested objects are shared between the original and copied instances.
- How Do deepcopy and Shallow Copy Affect Nested Objects in Python?
Shallow Copy: Copies only the outer object and keeps references to nested objects, so modifications to nested objects are reflected in both the original and copied objects.
Deep Copy: Creates copies of all nested objects, so the original and copied objects are entirely separate, and changes to one do not affect the other.

```
4. What is destructor
5. List vs Tuple memory management

### Capgemini AWS-Python Profile 
**1st Round [20th June 2022] [Cleared]**

- Python and SQL:

1. Shallow vs Deep Copy
2. Remove duplicates in a column without using distinct
```
select plan_num from temp_table
qualify row_number() over (partition by plan_num order by plan_num) = 1;

** Same result without distinct. Row number will assign a unique number for same entries therefore we can get the row number = 1 to get all the unique entries.
** Qualify is nothing but similar to Where and Having clauses but for window functions.
```
3. Adding two dataframes in pandas
```
Two commands can be used are:
pandas.concat(objs, *, axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None, verify_integrity=False, sort=False, copy=None)
pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=None, indicator=False, validate=None)
```
- Reference: [Pandas Docs](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)

4. Reversing a string
```
## Reverse a sentence
## Input: "my name is aditya"
## Required output: aditya is name my

new = "my name is aditya"
temp = " ".join(new.split()[::-1]) 
print("Reversed list: ",temp)
## .split() will split each word, [::-1]: reverse order, " ".join(): join list every element with a space
## temp will be a list before join, after join becomes a string.
```
5. Map,filter,reduce and lambda functions.
```
from functools import reduce

n = [1,2,3,4,5,10,11]
# ------------------------------------------------------

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
print((lambda x:x+5)(6)) 

# ---------------------------------------------------
print(list(filter(lambda x:x%2==0,n)))
# filter(function or None, iterable) --> filter object
# Return an iterator yielding those items of iterable for which function(item)
# is true. If function is None, return the items that are true.


# -----------------------------------------------
## map(func, *iterables) --> map object
## Make an iterator that computes the function using arguments from
## each of the iterables. Stops when the shortest iterable is exhausted.

print(list(map(lambda x:x*2,n)))
# --------------------------------------------

## Reduce: cummalative function to reduce the iterable to a single value
print(reduce(lambda x,y:x+y,n))

## reduce(function, sequence[, initial]) -> value

# Apply a function of two arguments cumulatively to the items of a sequence,
# from left to right, so as to reduce the sequence to a single value.
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
# ((((1+2)+3)+4)+5). If initial is present, it is placed before the items
# of the sequence in the calculation, and serves as a default when the
# sequence is empty.
```
- Reference:
[Map Functions](https://youtu.be/8q2vICb89ys?si=-PeggfFs8P-aVRn5),  
[Lambda Functions](https://youtu.be/KR22jigJLok?si=pcVa_jqHhos5jfFA)
7. List slicing vs split
```
## List Split
random_string = "Hey, there. How are you?"
lst3 = random_string.split(" ")
print("Split List:",lst3)
## .split(<separator>): separator can be anything. comma,semicolon etc.
# Output: Split List: ['Hey,', 'there.', 'How', 'are', 'you?']


## List Slicing:
#  syntax: list_name[start_index:end_index:jump]: end_index is not included
print("List slicing:",lst[1:3:1])
print("Reversed List using slicing:",lst[::-1])

##Output:
## List slicing: [2, 3]
## Reversed List using slicing: [5, 4, 3, 2, 1]

```
8. functions in strings
9. List Comprehension
```
lst = [1,2,3,4,5,10,12,90]
## List comprehension
### Case 1: Create a list which is squared of each number

lst1 = [x*2 for x in lst]
print(lst1)

### Output:[2, 4, 6, 8, 10, 20, 24, 180]

### Case 2: Create a list which check another list: if iterator is even put 0 else put 1

lst2 = [ 1 if x%2==0 else 0 for x in lst]
print(lst2)
### Output: [0, 1, 0, 1, 0, 1, 1, 1]
```

- AWS:

1. EC2
```
Amazon Elastic Compute Cloud (Amazon EC2) provides on-demand, scalable computing capacity in the Amazon Web Services (AWS) Cloud. Using Amazon EC2 reduces hardware costs so you can develop and deploy applications faster. You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. You can add capacity (scale up) to handle compute-heavy tasks, such as monthly or yearly processes, or spikes in website traffic. When usage decreases, you can reduce capacity (scale down) again.

An EC2 instance is a virtual server in the AWS Cloud. When you launch an EC2 instance, the instance type that you specify determines the hardware available to your instance. Each instance type offers a different balance of compute, memory, network, and storage resources.
```
- Reference: [EC2 AWS Doc](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)

2. S3
- Reference: [S3 AWS Doc](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
3. Elastic BeanStalk
4. Lambda [Use Cases]
5. IAM role importance
6. SQS, SNS services
7. Different types of services in AWS
8. Global and region services in AWS

```
sol: 
- Global Services: Services that has global in the region specification area

1. AWS IAM
2. Amazon S3
3. Amazon Route 53
4. Amazon CloudFront

- Region Specific: Services that requires you to specify a region:

1. Amazon EC2
2. AWS Lambda
3. RDS
4. DynamoDB
etc.....
```

9. Storage limit in AWS S3 bucket

sol: The total volume of data and number of objects you can store are unlimited. Individual Amazon S3 objects can range in size from a minimum of 0 bytes to a maximum of 5 TB. The largest object that can be uploaded in a single PUT is 5 GB. For objects larger than 100 MB, customers should consider using the Multipart Upload capability.



10. How do you use s3 services
11. Other storage services in AWS apart from s3

```
sol:
1. S3 Glacier
2. Elastic Block Store (EBS)
3. Elastic File System (EFS)
4. Amazon Storage Gateway
5. Snowball
6. Snowmobile

```

**2nd Round [24th June 2022] [Cleared]**

1. A basic pattern program
2. ETL experience
3. Some agile based questions
4. CI/CD pipeline
5. Libraries in python you have used.
6. Lambda functions
7. Step functions

**3rd Round (Client Interview) [29th June 2022] [Cleared]**

1. 5th highest salary in a table of employees.
2. Basic experience of agile, ETL and release
3. Basic Intro of client and project

**4th Round [30th June 2022] [Cleared]**

- Amcat based english test (30 minutes)



### Octros Technical Round [22nd June]
**[Failed]**

1. Valid parenthesis

- References:
1. [NeetCode](https://youtu.be/WTzjTskDFMg)
2. [LeetCode Question](https://leetcode.com/problems/valid-parentheses/)

```
#Valid Parenthesis:
## Algorithm:



# Step1: Create a dictionary which has closing bracket as a key and value as open bracket.
# Step2: Iterate over string
# Step3: Check if stack has anything and top most element of stack has open bracket of iterating bracket, If yes remove that
# Step4: Else return false [Brackets are imbalance]
# Step5: If it is an open bracket just add it into the stack
# Step6: Return true if stack is empty or false if not

str = "((()))"
str2 = ")))((("
str3 = "[)[)"

def isValid(s: str):
    stack = []
    closeToOpen = {")":"(","}":"{","]":"["}
    
    for i in s:
        if i in closeToOpen:
            if stack and stack[-1] == closeToOpen[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False
        

test = isValid(str3)
print(test)

## Time Complexity: O(n)
## Space Complexity: O(n)
```


2. Finding out three numbers in a given list whose sum is equal to a given number
3. How to do Authentication in python
4. Token generation process in django or flask
