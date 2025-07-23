class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        res = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
                res = mid
            else:
                right = mid - 1
        return res

solution = Solution()
print(solution.mySqrt(4))
print(solution.mySqrt(8))