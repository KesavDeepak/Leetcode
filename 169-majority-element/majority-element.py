class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Boyes - Moore Algorithm
        res, c = 0,0
        for i in nums:
            if c == 0:
                res = i
            if res == i:
                c+=1
            else:
                c-=1
        return res

        