class Solution(object):
    def distributeCookies(self, cookies, k):
        """
        :type cookies: List[int]
        :type k: int
        :rtype: int
        """
        
        best_max = float('inf')

        def distributeDFS(bag, distributions):
            nonlocal best_max

            if bag == len(cookies):
                # base case - cookies have all been distributed (return )
                best_max = min(best_max, max(distributions))
                return

            for child in range(len(distributions)):        
                # give child cookies & find new max
                distributions[child] += cookies[bag]
                curr_max = max(distributions)

                # progress down branch if child still has 
                if curr_max < best_max:

                    distributeDFS(bag + 1, distributions)
                
                # undo after doing comparison
                distributions[child] -= cookies[bag]
        
        distributeDFS(0, [0] * k)
        return best_max
