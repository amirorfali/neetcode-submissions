class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=s.replace(" ", "")
        s=[i for i in s if i.isalnum()]
        s="".join(s)
        print(s)
        t=""
        for i in range(len(s)-1,-1,-1):
            if s[i].isalnum():
                t+=f"{s[i].lower()}"
        return t==s 