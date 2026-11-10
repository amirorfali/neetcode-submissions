class Solution:

    def encode(self, strs: List[str]) -> str:
        string=""
        for word in strs:
            string+=str(len(word))+"#"+word
        return string
        
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":        # find the '#' that ends the number
                j += 1
            length = int(s[i:j])      # digits between i and j
            word = s[j + 1 : j + 1 + length]
            ans.append(word)
            i = j + 1 + length        # jump to the start of the next number
        return ans
                            
            