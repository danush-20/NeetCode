class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = list(s)
        t = list(t)
        l.sort()
        t.sort()
        return l == t
        
        
        