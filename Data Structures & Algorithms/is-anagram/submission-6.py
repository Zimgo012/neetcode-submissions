class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        a = "".join(sorted(s)) + "".join(sorted(t, reverse=True))
        
        L = 0
        R = len(a) - 1

        while L < R:
            if a[L] == a[R]:
                L+=1
                R-=1
            else :
                return False
        return True        