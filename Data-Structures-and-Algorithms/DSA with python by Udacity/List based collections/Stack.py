

# Implementing stack in python will require the knowledge of Object Oriented
# programming(OOP's)
# Not very much just the basics of Class and objects.

#STACK =LIFO(Last In First Out)


class ArrayStack:
# ArrayStack is a class
# Now we will make various functions for performing some basic tasks
# like push,pop,top,len and etc.

    
    def __init__(self):
        self.A=[]
    def __len__(self):
        return len(self.A)
    def is_empty(self):
        return len(self.A)==0
    def push(self,key):
        self.A.append(key)
    def pop(self):
        if self.is_empty():
            print('the Stack is empty')
        else:
            self.A.pop()
    def top(self):
         if self.is_empty():
            print('the Stack is empty')
         return self.A[-1]

   # Clearly -1 index is of the last element inserted
   # without the need to find the total length of the stack.

# Now we will make an object:
a=ArrayStack()
# object is made by calling the class

# now we have to insert the element
a.push(25)
#[25]
a.push(30)
#[25,30]
a.push(90)
#[25,30,90]
print("The Stack is:",a.A)
#[25,30,90]
print("Pop the Stack:",a.pop())
print("Now the Stack is:",a.A)
#[25,30]
print("Pop the Stack:",a.pop())
print("Now the Stack is:",a.A)
#[25]
print("Pop the Stack:",a.pop())
print("Now the Stack is:",a.A)
#[]

print('_____________________')
a.push(25)
a.push(30)
a.push(90)
print('After Pushing Now the Stack is:',a.A)
print("The Top of the Stack is :",a.top())
print('The Length of the Stack is:',len(a))



