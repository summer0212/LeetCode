class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        char_set = set()
        max_length = 0

        for right in range(0,len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length,len(char_set))
        # print(char_set)
        return max_length


object = Solution()
print(object.lengthOfLongestSubstring(s = "abcabcbb"))