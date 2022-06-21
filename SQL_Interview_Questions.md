## Important SQL QUESTIONS

References:
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

- Reference: [Video tutorial on RowNumber,Partition,Rank and DenseRank](https://youtu.be/QFj-hZi8MKk)

3. Views
4. Triggers
5. Stored procedures

6. Remove duplicates in a column without using distinct