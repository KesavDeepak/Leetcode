class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0 , len(s)-1
        while l <r :
            if s[l] != s[r]:
                siL, siR = s[l+1:r+1],s[l:r]
                siL = (siL[::-1] == siL)
                siR = (siR == siR[::-1])
                return siL or siR
            l,r = l+1, r-1
        return True
        