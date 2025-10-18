class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res,quad = [],[]
        def KSum(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-k+1):
                    if i>start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    
                    KSum(k-1,i+1,target-nums[i])

                    quad.pop()
                return
            l,r = start,len(nums)-1
            while l<r:
                curr = nums[l]+nums[r]
                if curr > target:
                    r-=1
                elif curr < target:
                    l+=1
                else:
                    res.append(quad+[nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
        KSum(4,0,target)
        return res        