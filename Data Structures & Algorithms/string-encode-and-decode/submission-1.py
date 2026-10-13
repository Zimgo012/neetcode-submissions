class Solution:

    def encode(self, strs: List[str]) -> str:
            if not strs:
                return ""
            encode = ""
            num = 0
            tempWord = ""
            for s in strs:
                num = len(s)
                tempWord += str(num) + "#"
                
                for c in s:
                    tempWord += c
                
                encode += tempWord 
                tempWord = ""
                num = 0

            print(encode)
            return encode



        

    def decode(self, s: str) -> List[str]:
        
        listWord = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            listWord.append(s[j+1 : j + 1 + length])

            i= j + 1 + length

        return listWord

             
