# Word Pattern 2020
class Solution:
    def checkIfEqual(self, values: list, words: list) -> bool:
        first_word = words[values[0]]
        for el in values:
            if first_word != words[el]:
                return False
        return True

    def checkThatUnique(self, indices: dict, words: list) -> bool:
        starting_indices = []
        for key in indices:
            starting_indices.append(indices[key][0])

        if len(starting_indices) == 1:
            return True

        for i in range(len(starting_indices)):
            for j in range(i + 1, len(starting_indices)):
                if words[starting_indices[i]] == words[starting_indices[j]]:
                    return False

        return True

    def wordPattern(self, pattern: str, string: str) -> bool:
        words = string.split()
        indices = {}

        for i in range(len(pattern)):
            if pattern[i] in indices:
                indices[pattern[i]].append(i)
            else:
                indices[pattern[i]] = [i]

        if len(words) != len(pattern):
            return False

        for key in indices:
            if not self.checkIfEqual(indices[key], words):
                return False

        if not self.checkThatUnique(indices, words):
            return False
        return True

# Solution 2025
class Solution2(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        split = s.split()
        matching_dict = {}
        visited = set()

        if len(split) != len(pattern):
            return False

        for i in range(len(pattern)):
            curr_symbol = pattern[i]
            curr_word = split[i]

            if curr_symbol in matching_dict:
                # check that value matches what key pulls
                if matching_dict[curr_symbol] != curr_word:
                    return False
            else:
                # add symbol
                if curr_word in visited:
                    return False

                matching_dict[curr_symbol] = curr_word
                visited.add(curr_word)
        
        return True
