## Important SQL QUESTIONS

- References:
1. [53 Imp. Questions SQL](https://youtu.be/pKFo8Mqp-cU)
2. [SQL Interview Questions Interview Bit](https://www.interviewbit.com/sql-interview-questions/)

<!-- ------------------------------------------------------- -->

1. Nth highest salary:

- CASE 1: Using limit only
```
sol: select salary from employee order by salary desc limit n-1,1;
```

- Explanation: As indexing starts from zero therefore if we have to find out the second highest salary then we put limit 1,1. 
The first integer after limit keyword is index and second one is number of records needed.
for example: if we have to find out 2nd and 3rd highest we can write **limit 1,2**.

CASE 2: Using offset

```
sol: select salary from employee order by salary limit 1 offset n-1;
```
Explanation: Here limit 1 means 1 record and after offset just put the index of salary you want. for example if we need
third highest salary we will write **offset 2**.

2. Row_number vs Partition vs Rank vs Dense Rank

sol: 
- RANK() assigns the same rank with gaps for equal values.
- DENSE_RANK() assigns the same rank without gaps for equal values.
- ROW_NUMBER() assigns a unique rank to each row.

Explanation: rank creates unique number for different records but same number for same records. Keeping in mind rank will skip the numbers if there are duplicate records for eg.
if there are duplicates they will get same rank(let's say 4) and next rank will be given as 6 considering there are just two values at rank 4.

Dense rank does the same work except it doesn't skip the number. For the same example given above if two records have rank 4 so the next rank would be 5.


```
SYNTAX:

select 
Row_Number() over (order by salary desc) RowNumber,
Row_Number() over (partition by some_column order by salary desc) partNumber,  
rank() over (order by salary desc) RankId,  
dense_rank() over (order by salary desc) DenseRank 
from Employee

```
- Article: (https://www.naukri.com/code360/library/difference-between-rank-and-denserank)
- Reference: [Video tutorial on RowNumber,Partition,Rank and DenseRank](https://youtu.be/QFj-hZi8MKk)

3. Views
4. Triggers
5. Stored procedures

6. Remove duplicates in a column without using distinct

sol:
```
1. select unique emp_name from employee;

2. select emp_name from employee group by emp_name;

3. select emp_name from employee union select emp_name from employee;
```
- Reference: [How To Get unique records without using distinct in oracle](https://youtu.be/2G8zuE5JuUA)


