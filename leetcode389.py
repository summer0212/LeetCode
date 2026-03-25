from collections import Counter

class Solution:
    def findTheDifference(self, s, t) :
        count_of_s = Counter(s)
        result = ""
        print("The dict of s ",count_of_s)

        for char in t:
            if count_of_s[char] == 0:
                result = char
            
            count_of_s[char] -= 1

        return result

object = Solution()
print(object.findTheDifference(s = "a", t = "aa"))
        