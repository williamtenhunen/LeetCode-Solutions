from typing import Optional, List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0        
        k = 1        
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k

def judge(nums):
    expected = sorted(set(nums))
    k = Solution().removeDuplicates(nums)
    assert k == len(expected)
    assert nums[:k] == expected
    print("✓ passed")

judge([1,1,2])
judge([0,0,1,1,1,2,2,3,3,4])
judge([-100,-100,0,0,100])