class Solution:
    def findPermutationDifference(self, s, t) :
        sum = 0
        for i in range(len(s)):
            if s[i] in t:
                # print(t.index(s[i]),"for",s[i])
                diff = abs(i - t.index(s[i]))
                sum += diff
        return sum
        
object = Solution()
print(object.findPermutationDifference("abc", "acb"))