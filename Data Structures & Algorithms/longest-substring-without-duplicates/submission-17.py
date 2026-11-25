class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        ans=1
        l=0
        if len(s)==0: return 0

        for r in range(len(s)):
            #print(s[r])
            while s[r] in seen:
                #rint(seen)
                seen.remove(s[l])
                l+=1
                
            seen.add(s[r])
            ans=max(ans, r-l+1)
            
        
        return ans



