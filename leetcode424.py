'''Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''
from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_dict = {}
        # right = 0
        left = 0
        max_length = 0

        for right in range(0,len(s)):
            char = s[right]

            s_dict[char] = s_dict.get(char,0) + 1
            max_freq = max(s_dict.values())

            while (right - left + 1) - max_freq > k:
                left_char = s[left]
                s_dict[left_char] -= 1
                left += 1

                max_freq = max(s_dict.values())

            max_length = max(max_length, right - left + 1)

        return max_length
    
object = Solution()
print(object.characterReplacement(s = "AABABBA", k = 1))