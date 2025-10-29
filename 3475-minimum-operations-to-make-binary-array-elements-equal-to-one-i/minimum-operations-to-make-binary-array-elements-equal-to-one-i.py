class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        def flip(val):
            if val == 0:
                val = 1
            else:
                val = 0
            return val
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] = flip(nums[i+1])
                nums[i+2] = flip(nums[i+2])
                c = c+1
        if nums.count(0) <= 0:
            return c
        else:
            return -1

