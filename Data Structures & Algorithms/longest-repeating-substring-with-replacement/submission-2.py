class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1          # grow: add the new letter

            while (r - l + 1) - max(count.values()) > k:   # too many letters to replace?
                count[s[l]] -= 1                           # shrink: drop the leftmost letter
                l += 1

            ans = max(ans, r - l + 1)

        return ans