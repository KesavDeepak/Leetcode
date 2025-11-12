class Solution:
    def mySqrt(self, x: int) -> int:
        if x <=0 or x> ((2**31) -1):
            return 0
        
        approx = 0.5*x
        better = 0.5*(approx + x/approx)
        while better != approx:
            approx = better
            better = 0.5*(approx + x/approx)
        return int(better)
        