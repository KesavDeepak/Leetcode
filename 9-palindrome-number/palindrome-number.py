class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False
        res =0
        n = x
        while n !=0:
            res = res*10+(n%10)
            n = n//10
        return res == x
            
            

        