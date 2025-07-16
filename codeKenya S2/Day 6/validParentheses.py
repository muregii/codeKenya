class Solution:
    def isValid(self, s: str) -> bool:
        #   UMPIRE
        # UNDERSTAND

        # MATCH -> Stacks

        #PLAN /strategy

        #start with s = "[]" 
        #declare a stack
        # s = []
        #If i find '[', I'll add it to a pre-initialized stack
        #stack = [''] T or F
        #what if it's a closing ']', 
        #stack = ["["]
        #if my stack is empty or first char in our stack is not an '['  -> return False
        #else remove char from stack.

        # IMPLEMENTATION
        #1. Time O(n) linear time complexity 2. Space O(n)
        stack = [] #O(1)
        #s = ((((((
        for char in s: #O(n)
            if char == '[' or char == '{' or char == "(": #O(1)
                stack.append(char) #O(1) LIFO
            elif char == ']':#O(1)
                if not stack or stack[-1] != '[':#O(1)
                    return False#O(1)
                stack.pop()#O(1)
            elif char == '}':#O(1)
                if not stack or stack[-1] != '{':#O(1)
                    return False#O(1)
                stack.pop()#O(1)
            elif char == ')':#O(1)
                if not stack or stack[-1] != '(':#O(1)
                    return False#O(1)
                stack.pop()#O(1)
            else:#O(1)
                return False#O(1)
        return not stack#O(1)
        #1  Drop constants
        #2. Leading terms matter

#REVIEW
#EXPAND
s = "([{}])"
print(Solution().isValid(s))
                



 
        
        

            

      


        