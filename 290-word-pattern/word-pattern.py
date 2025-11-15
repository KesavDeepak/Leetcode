class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words)!= len(pattern):
            return False
        wordtcount = {}
        counttword = {}
        for c,w in zip(pattern,words):
            if c in wordtcount and wordtcount[c] != w:
                return False
            if w in counttword and counttword[w] != c:
                return False
            wordtcount[c] = w
            counttword[w] = c
        return True
            
        