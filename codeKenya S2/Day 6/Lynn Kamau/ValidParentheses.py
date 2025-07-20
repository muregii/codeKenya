# Valid Parentheses Leetcode Challenge
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    bracket_map = {')': '(', ']': '[', '}': '{'}
    stack = []

    for char in s:
        if char in bracket_map.values():  
            stack.append(char)
        elif char in bracket_map:  
            if not stack or stack[-1] != bracket_map[char]:
                return False 
            stack.pop()  

    return not stack 


#TEST CASES
print(isValid("()"))        
print(isValid("(]"))        
print(isValid("([)]"))    
print(isValid("{[]}"))     
print(isValid("["))

