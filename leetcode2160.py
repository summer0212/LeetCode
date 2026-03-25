
class Solution:
    def countConsistentStrings(self, allowed, words):
        count = 0
        for word in words:
            is_word_good = True
            for char in word:
                if char not in allowed:
                    is_word_good = False
                    break

            if is_word_good == True:
                count += 1
        return count
    
object = Solution()
print(object.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))


        