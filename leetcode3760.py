class Solution:
    def maxDistinct(self, s: str) -> int:
        s_set = set(s)
        return len(s_set)
    
object = Solution()
print(object.maxDistinct(s = "abcde"))