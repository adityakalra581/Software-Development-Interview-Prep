



#HackerRank Link: https://www.hackerrank.com/challenges/equality-in-a-array/problem
#!/bin/python3

def equalizeArray(arr):
    # Write your code here
    count = {}
    for i in arr:
        if i not in count.keys():
            count[i] = 1
        else:
            count[i] += 1
    return len(arr)-max(count.values())

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = equalizeArray(arr)
