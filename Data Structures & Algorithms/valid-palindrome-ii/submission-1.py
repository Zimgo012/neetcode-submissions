class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s) - 1

        while i < j:

            if s[i] != s[j]:
                # we will skip the L pointer
                # ex: abbda
                # skipL = bda
                #        i^^j  
                skipL = s[i + 1 : j + 1]
            
                # we will skip the R pointer 
                # ex:  abbda
                # skipR = abb
                #         i^^j - True
                skipR =  s[ i : j]

                # we retrun if theres a possible match betwee slices
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            i += 1
            j -= 1
        return True
                

