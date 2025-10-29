class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i+1] = 1-nums[i+1]
                nums[i+2] = 1 - nums[i+2]
                c = c+1
        if nums.count(0) <= 0:
            return c
        else:
            return -1

