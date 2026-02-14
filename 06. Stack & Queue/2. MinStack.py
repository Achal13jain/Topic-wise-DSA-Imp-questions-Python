"""
Problem: Min Stack
LeetCode: https://leetcode.com/problems/min-stack/

Time Complexity: O(1) for all operations
Space Complexity: O(n)
Why optimal: Two-stack approach allows keeping track of the minimum at every state in constant time.
"""

# Design a stack that supports:
# push
# pop
# top
# getMin
# 👉 All in O(1) time

# 🔹 Idea (Two Stacks)
# Main stack → stores values
# Min stack → stores current minimum at each level

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        # Push minimum so far
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            val = self.stack.pop()

            # If popped value is current minimum
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
# Example usage
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())  # Output: -3
min_stack.pop()
print(min_stack.top())     # Output: 0
print(min_stack.getMin())  # Output: -2

# Time Complexity: O(1) for all operations
# Space Complexity: O(n) for stacks