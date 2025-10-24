class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s)>2):
            r = ""
            for j in range(len(s)-1):
                r+= str(((int(s[j])+int(s[j+1]))%10))
            s = r
        return s[0] == s[1]       
