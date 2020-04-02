## Read firstclass_functions --> Closures.

## Closures: In programming languages, a closure, 
# also lexical closure or function closure, is a technique for implementing 
# lexically scoped name binding in a language with first-class functions. 

# Operationally, a closure is a record storing a function together with an environment.

# The environment is a mapping associating each free variable of the function 
# (variables that are used locally, but defined in an enclosing scope) with the value 
# or reference to which the name was bound when the closure was created. Unlike
# a plain function, a closure allows the function to access those captured variables
# through the closure's copies of their values or
# references, even when the function is invoked outside their scope.

## Article: https://sethirajat.com/closures-in-depth/



## CASE 1: Returning without Execution(That means returning a function with a function without parenthesis)

def satire():                            ## An outer function
    message = "Howdy"
    def sat():                            ## An Inner Function
        print(message)
    return sat

## Assigning without parenthesis:
free = satire
print(free.__name__)
# # Output: satire

print(free())
## OUTPUT: <function satire.<locals>.sat at 0x0000021004275EE0>


temp = satire()
print(temp.__name__)
# sat
## See closely: if we give parenthesis to the function(outer) the variable is assigned to Inner function. 

temp()
#Howdy

## And still inner function remembers the message "Howdy". This is the Concept of Closure.
## Rememberance of value beyond it's scope.






# **********************************************************

## CASE 2: Returning with Execution(That means returning a function with a function with parenthesis)

def something():                            ## An outer function
    message = "Howdy"
    def some():                            ## An Inner Function
        print(message)
    return some()

## Assigning without parenthesis:
free = something
print(free.__name__)
# # Output: something     [Parent or Outer Function]

free()
## OUTPUT: Howdy
## Simple difference, With parenthesis calling a function will give the answer.


## Check whether closure concept will work here:

temp = something()

## This will be Executed and provide output "Howdy".

# print(temp.__name__)
## Will not work, as it does not store anything ["None Type"] 


