class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofsquare(n):
            s =0
            while n>0:
                s = s+((n%10)**2)
                n = n//10
            return s

        visit = set()
        while n not in visit:
            visit.add(n)
            n = sumofsquare(n)

            if n ==1:
                return True
        return False






            

