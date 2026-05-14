class Solution:
    def sortSentence(self, s: str) -> str:
        res = [""] * 10
        l = 0
        curr = ""
        for i in range(len(s)):
            if s[i] == ' ': continue 

            curr += s[i]
            c = s[i]

            if ord(c) <= ord('9'):
                idx = int(c)
                res[idx - 1] = curr[:-1]

                curr = ""
                l += 1
        
        res = " ".join(res[:l])

        return res
