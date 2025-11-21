class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        i = 0
        while i < len(nums):
            if original in nums:
                original *=2
            i = i+1
        return original