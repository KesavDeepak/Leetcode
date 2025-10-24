class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        while n!=0:
            c = b
            b = a+b
            a = c
            n -=1
        return a


