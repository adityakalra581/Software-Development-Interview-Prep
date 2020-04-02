## First Class Functions: 

# In computer science, a programming language is said to have first-class functions if it treats functions as 
# first-class citizens, this means the language supports passing functions as arguments to other functions,
# returning them as the values from other functions, and assigning them to variables or storing them 
# in data structures.

# Some programming language theorists require support for anonymous functions (function literals) as well.
# In languages with first-class functions, the names of functions do not have any special status;
# they are treated like ordinary variables with a function type. 

## For Example:

def twice(x):
    return 2*x

## Treating function as variable.
double = twice
# Just initiating the function and not executing it right now.


print(twice(2))

####
#    OUTPUT:
#    4






## Higher Order Functions:

# First-class functions are a necessity for the functional programming style, 
# in which the use of higher-order functions is a standard practice.
 
# A simple example of a higher-ordered function is the map function, 
# which takes, as its arguments, a function and a list, and returns the list 
# formed by applying the function to each member of the list. For a language 
# to support map,it must support passing a function as an argument.

## Example for Higher order function:

def mapping(func,list):
    out = []
    for i in list:
        out.append(func(i))
    return out

x = mapping

print(mapping(twice,[1,4,5,6]))

## OUTPUT : [2, 8, 10, 12]

