
def balancedParentheses(s: str) -> bool:
    stack = []

    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
        
    return len(stack) == 0

print(balancedParentheses("bloomberg()"))

