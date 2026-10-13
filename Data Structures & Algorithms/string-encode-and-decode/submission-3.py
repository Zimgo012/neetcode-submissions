class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        res = ""
        indexNum = 0
        tempWord = "" 

        for s in strs:
            indexNum = len(s)
            tempWord = str(indexNum) + "#" + s

            res += tempWord

            indexNum = 0
            tempWord = ""
        return res
        

    def decode(self, s: str) -> List[str]:
        output = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j + 1 : j + 1 + length])

            i = j + 1 + length
        return output


