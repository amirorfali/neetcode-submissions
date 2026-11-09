class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        dict2={}

        for i in range(len(s)):
            dict1[s[i]]=dict1.get(s[i],0)+1
        
        for j in range(len(t)):
            dict2[t[j]]=dict2.get(t[j],0)+1
        
        
        return dict1==dict2