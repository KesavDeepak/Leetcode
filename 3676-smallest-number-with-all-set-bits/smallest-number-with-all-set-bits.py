class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 1
        while (n > (2**i)-1):
            i+=1
        return (2**i)-1
