class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        n = len(nums1)
        if(n%2==0):
            m = n//2
            p = m-1
            return ((nums1[m]+nums1[p])/2)
        else:
            m = n//2
            return nums1[m]

        

        