class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x<0:
            neg = -1
            x=-x
        else:
            neg = 1
        
        r = 0
        
        while x!=0:
            r = r*10+(x%10)
            x = x//10
        if (r>-2**31 and r > (2**31) -1):
            return 0
        return neg*r
        
        