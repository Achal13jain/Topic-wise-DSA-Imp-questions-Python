#Check balanced paranthesis in a string

#Idea 
# Use a stack to keep track of opening paranthesis
# For every closing paranthesis, check if it matches the top of the stack
# If stack is empty at the end, paranthesis are balanced

def is_valid_parentheses(s):
    stack = []

    # Mapping closing → opening
    match = {')': '(', '}': '{', ']': '['}

    for ch in s:
        # Opening bracket
        if ch in match.values():
            stack.append(ch)
        else:
            # Closing bracket with no opening
            if not stack:
                return False

            top = stack.pop()
            if match[ch] != top:
                return False

    # Valid only if stack is empty
    return len(stack) == 0

# Example usage
s = "{[()]}"   
print(is_valid_parentheses(s))  # Output: True
s = "{[(])}"   
print(is_valid_parentheses(s))  # Output: False

# Time Complexity: O(n)
# Space Complexity: O(n)