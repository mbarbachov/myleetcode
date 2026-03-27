class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False 

        lf_1 = [0] * 26
        lf_2 = [0] * 26
        
        for i in range(len(s)):
            lf_1[ord(s[i]) - ord('a')] += 1
            lf_2[ord(t[i]) - ord('a')] += 1
        
        return lf_1 == lf_2

class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s.sort()
        t.sort()
