class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #count the number of non duplicates
        c =0 
        # checking whether a duplicate is present or not
        stack = []
        i=0
        while i < len(nums) and nums[i] != '_':
            if nums[i] in stack:
                nums.pop(i)
                nums.append('_')
                i = i-1
            else:
                stack.append(nums[i])
                c = c+1
            i = i+1
        return c

            
        

        