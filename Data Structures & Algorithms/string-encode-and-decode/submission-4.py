class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for word in strs:
            encoded+=f"#{len(word)}#{word}"
        print(encoded)
        return encoded
    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        j=1
        while i < len(s):
            if s[i]=='#':
                length=''
                while s[i+j]!='#':
                    length+=s[i+j]
                    j+=1
                    print(length)
                word=s[i+j+1:i+j+1+int(length)]
                ans.append(word)
                i=i+j+1+int(length)
                j=1
            else: return ans
        return ans

