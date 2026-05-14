class Solution:
    def findDuplicates(self, nums):
        repeats = dict()
        doubles = []

        for n in nums:
            if n in repeats:
                doubles.append(n)
                repeats[n] += 1
            else:
                repeats[n] = 1

        return doubles
    
    """
    no matter the length of the array we are garunteed that array is going to be at least n numbers long (n if no repeats, if repeats then n + len(repeats))
    using this fact we can treat elements from 1 to n as indicies 0 to n-1 and we can flip the sign to indicate that the number was "visited"
    i.e. [1, 1, 2] n = 2, when we search the first 1 the list becomes [-1, 1, 2] and then when you hit the next one the index 0 already holds -1
    this value could be negative x it does not matter as long as its negative, if negative then ans gets appended with the current num
    this tracks all duplicates given that it repeast at max 2 times without needing to make another list
    """
    def findDuplicatesOptimized(self, nums):
        # not my original solution but its more effecient on space [manipulates existing list based off constraints where numbers are [1, n]]
        ans = []

        for num in nums:
            # treat located number as the index and check to see if it was flipped
            num = abs(num)
            if nums[num - 1] < 0:
                # value (whatever it may be) is already negative so its a repeat
                ans.append(num)
            # flip index of visited value
            ans[num - 1] *= -1
        
        return ans
