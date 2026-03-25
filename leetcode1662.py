class Solution:
    def arrayStringsAreEqual(self, word1, word2) :
        word1_str = "".join(word1)
        word2_str = "".join(word2)

        # print(word1_str,word2_str)
        if word1_str == word2_str :
            return True
        return False
        
object = Solution()
print(object.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "cb"]))
        