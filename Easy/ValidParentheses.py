class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
    
        for char in s:
            if char in bracket_map:
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
    
        return not stack
    
solution = Solution()

print(solution.isValid("()"))
print(solution.isValid("()[]{}"))
print(solution.isValid("(]"))
print(solution.isValid("([])"))