## Valid Parenthesis:
## Algorithm:

## References:
# https://youtu.be/WTzjTskDFMg
# https://leetcode.com/problems/valid-parentheses/

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

