class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(ch for ch in s if ch.isalnum()).lower()
        st=0
        ed=len(s)-1
        while(st<=ed):
            if s[st]!=s[ed]:
                return False
            st+=1
            ed-=1
        return True