class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = 0
        l = 0
        
        while l < len(nums):
            if nums[l] == val:
                nums.pop(l)
            else:
                l = l+1
                c = c+1
        return c

                
            
