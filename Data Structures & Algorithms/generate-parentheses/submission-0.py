class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def build(s, open, close):
            if len(s) == 2 * n:          # full length, guaranteed valid
                ans.append(s)
                return
            if open < n:                 # rule 1: room for another "("
                build(s + "(", open + 1, close)
            if close < open:             # rule 2: an unclosed "(" to match
                build(s + ")", open, close + 1)

        build("", 0, 0)
        return ans