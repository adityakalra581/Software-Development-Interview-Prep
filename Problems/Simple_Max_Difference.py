n = int(input())
data = list(map(int,input().split(' ')))
print(data)
max_diff = -1

for i in range(n-1,-1,-1):
    record = data[i]

    for j in range(i):
        temp = record - data[j]
        if temp > max_diff and temp > 0:
            max_diff = temp


print(max_diff)
