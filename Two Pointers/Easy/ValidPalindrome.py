class Solution:
    def isPalindrome(self, s: str) -> bool:
        input = "".join(filter(str.isalnum,s)).lower()
        i=0
        j=len(input)-1
        while i<j:
            if input[i]!=input[j]:
                return False
            i+=1
            j-=1
        return True