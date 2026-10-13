class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode += str(len(s)) + "#" + s
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
    
        l = 0
        while l < len(s):
            r = l
            while s[r] != "#":
                r += 1
            length = int(s[l : r])
            decode.append(s[r + 1 : r + 1 + length])

            l = r +  1 + length
        return decode


