class Solution:
    def countConsistentStrings(self, allowed, words) :
        count = 0
        for char in allowed:
            for element in words:
                # print(element,"inside for loop")
                if char in element:
                    # print(element)
                    count += 1
        return count

object = Solution()
print(object.countConsistentStrings("abc",  ["a","b","c","ab","ac","bc","abc"]))