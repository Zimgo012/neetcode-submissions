class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freqS = {}
        freqT = {}

        for c in s:
            freqS[c] = freqS.get(c,0) + 1
        
        for c in t:
            freqT[c] = freqT.get(c,0) + 1

        return freqS == freqT



