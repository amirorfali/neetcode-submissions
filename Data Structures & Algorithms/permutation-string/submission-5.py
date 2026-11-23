class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        need = Counter(s1)               # letter counts of s1
        window = Counter(s2[:len(s1)])   # counts of the first window

        if window == need: return True

        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1                 # add the new letter on the right
            window[s2[r - len(s1)]] -= 1       # remove the letter that fell off the left
            if window == need: return True

        return False