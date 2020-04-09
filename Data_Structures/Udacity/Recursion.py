def fact(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return n*fact(n-1)



print(fact(5))
print(fact(3))
print(fact(-2))


## OUTPUT
# 120
# 6
# 0

#*************************************************

## Fibonacci using Recursion:

## 0,1,1,2,3,5,8,13,21,34,55 .......

## Logic:

#  answer = answer at previous position + ans at previous-1 position



def get_fib(position):
    if position <= 0:
        return  0
    elif position == 1:
        return 1
    return get_fib(position-1) + get_fib(position-2)


# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))

## OUTPUT:
# 34
# 89
# 0









