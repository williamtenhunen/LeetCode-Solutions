class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        return (x == x[::-1])
    
solution = Solution()

print(solution.isPalindrome(121))
print(solution.isPalindrome(122))