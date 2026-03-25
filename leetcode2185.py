class Solution:
    def prefixCount(self, words, pref):
        count = 0
        for word in words:
            # if pref in word:
            if word.startswith(pref):
                count += 1
        return count

object = Solution()
print(object.prefixCount(words =["leetcode","win","loops","success"], pref = "code"))