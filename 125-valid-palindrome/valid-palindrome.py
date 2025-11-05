class Solution:
    def isPalindrome(self, s: str) -> bool:
        #lowering the uppercase to lowercase
        s = s.lower()
        # Solving by two pointers
        l,r = 0, len(s)-1
        #Iterating the string
        while l <r:
            # checking whether the left pointer is a not a character or a number. if not a char then move the pointer else checking for the right and comparing the left pointer char and right pointer char
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
        