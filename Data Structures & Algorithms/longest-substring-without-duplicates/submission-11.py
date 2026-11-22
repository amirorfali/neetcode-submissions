class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        ans = 0

        for r in range(len(s)):
            while s[r] in seen:        # duplicate inside the window?
                seen.remove(s[l])      # drop the leftmost character
                l += 1                 # shrink from the left
            seen.add(s[r])             # now s[r] fits
            ans = max(ans, r - l + 1)  # window size

        return ans        