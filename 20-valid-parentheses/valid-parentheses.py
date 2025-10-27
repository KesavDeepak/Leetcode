class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in open:
                if stack and stack[-1] == open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
        