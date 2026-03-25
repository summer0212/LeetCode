# word = "ada"

# word_cleaned = word.lower()
# word_reverse = word[::-1]

# # print(reverse(word))

class Solution:
    def firstPalindrome(self, words):
        word_reverse = ""
        
        for i in range(0,len(words)):
            word_reverse = words[i][::-1]
            if words[i] == word_reverse:
                print(word_reverse)
                return words[i]
        return ""

object = Solution()
print(object.firstPalindrome(words = ["def","ghi"]))
