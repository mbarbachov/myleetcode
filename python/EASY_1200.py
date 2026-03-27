class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(arr)
        minDiff = abs(arr[-1] - arr[-2])
        ans = []

        for i in range(len(arr) - 1, 0, -1):
            if abs(arr[i] - arr[i - 1]) < minDiff:
                # update min diff
                minDiff = abs(arr[i] - arr[i - 1])
        
        for i in range(0, len(arr) - 1):
            if abs(arr[i + 1] - arr[i]) == minDiff:
                ans.append([arr[i], arr[i + 1]])
    
        return ans
    
    def minimumAbsDifference2(self, arr):
        # dictionary implementation allowing for O(1) lookup -> less effecient 
        arr = sorted(arr)
        minDiff = float('inf')
        answDict = {}
        
        for i in range(len(arr) - 1):
            diff = abs(arr[i + 1] - arr[i])
            if minDiff > diff: minDiff = diff
            
            if diff in answDict: answDict[diff].append([arr[i], arr[i + 1]])
            else: answDict[diff] = [[arr[i], arr[i + 1]]]
        
        return answDict[minDiff]
            
