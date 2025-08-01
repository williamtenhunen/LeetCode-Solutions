class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        
        return ''.join(reversed(result))

solution = Solution()
print(solution.addBinary("11", "1"))
print(solution.addBinary("1010", "1011"))