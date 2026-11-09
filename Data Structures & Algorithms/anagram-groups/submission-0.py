class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            count = [0]*26            # fresh counter for THIS word
            for c in word:
                count[ord(c)-ord('a')]+=1                
            key = "".join(sorted(word))              
            groups[key].append(word)

        return list(groups.values())