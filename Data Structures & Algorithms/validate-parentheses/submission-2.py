class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == ')' or c == '}' or c == ']':
                if len(stack) == 0:
                    return False
                char = stack.pop()
                if char == '(' and c != ')':
                    return False
                if char == '{' and c != '}':
                    return False
                if char == '[' and c != ']':
                    return False
            else:
                stack.append(c)
        return True