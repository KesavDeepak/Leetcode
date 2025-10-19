class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        neg = -1 if x<0 else 1
        r = 0
        x = abs(x)
        while x!=0:
            r = r*10+(x%10)
            x = x//10
        if (r>-2**31 and r > (2**31) -1):
            return 0
        return neg*r
        
        