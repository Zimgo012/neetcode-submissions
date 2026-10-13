class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        previousword = ""

        "luffy is still joyboy"

        for i in range(len(s)):

            if s[i] != " ":
                if i > 0 and s[i-1] == " ":
                    previousword = ""
                previousword += s[i]
            else:
                continue
        return len(previousword)