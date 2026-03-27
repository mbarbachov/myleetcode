class Solution(object):
    def lastVisitedIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = []
        ans = []
        k = 0

        for n in nums:
            if n == -1:
                # negative one
                k += 1
                if k <= len(seen):
                    # find element of seen 
                    ans.append(seen[k - 1])
                else:
                    ans.append(-1)
            else:
                # positive number
                seen.insert(0, n)
                k = 0
        
        return ans

# Passed 706 test cases -> 3ms (OFFICIAL 0MS SOlUTION is done via dequeue):

