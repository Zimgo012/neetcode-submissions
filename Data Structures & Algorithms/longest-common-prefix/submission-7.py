class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = ""
        ref = strs[0]

        for i in range(len(ref)):
            for s in strs:
                if len(s) == i or s[i] != ref[i]:
                    return res
            res += s[i]
        
        return res