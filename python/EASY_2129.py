class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title = title.lower().split()   # split the title into individual words ' ' being the default seperator
        result = ""

        for i in range(0, len(title)):
            w = title[i]
            if len(title[i]) > 2:
                # word is longer than two letters
                result += w[0].upper() + w[1:]
                if i != len(title) - 1: result += " "
            else:
                # word is shorter than 3 letters 
                result += w
                if i != len(title) - 1: result += " "
            
        return result


test = Solution()

print(test.capitalizeTitle("tHIS is a TEST"))
print(test.capitalizeTitle("alll lower case"))
print(test.capitalizeTitle("ALL UPPER CASE"))
print(test.capitalizeTitle("sh or t wo rd s no ca pi ta ls"))
print(test.capitalizeTitle("ONELONGWORD"))
print(test.capitalizeTitle("tHIS is a ST"))
