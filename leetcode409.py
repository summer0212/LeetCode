from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dict = Counter(s)

        palindrome_len = 0
        has_odd_char = False

        for val in s_dict.values():
            if val % 2 == 0:
                palindrome_len += val

            else:
                palindrome_len += val - 1
                has_odd_char = True

        if has_odd_char:
            palindrome_len += 1

        return palindrome_len
    
object = Solution()
print(object.longestPalindrome(s = "a"))

'''Formula method:
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        length = 0
        for i in count.values():
            length+=(i//2)*2
        if length < len(s):
            length+=1
        return length'''