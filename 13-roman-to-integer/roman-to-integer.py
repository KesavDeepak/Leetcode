class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i in range(len(s)):
            if (i+1 <len(s) and a[s[i]] < a[s[i+1]]):
                res -= a[s[i]]
            else:
                res += a[s[i]]
        return res

        