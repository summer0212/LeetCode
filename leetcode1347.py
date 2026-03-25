#An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # Step 1: Count the frequencies of characters in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        steps = 0
        
        # Step 2: Check every character required by 's'
        for char in count_s:
            # How many of this character does 's' need?
            needed = count_s[char]
            
            # How many of this character does 't' actually have?
            # (If 't' doesn't have it at all, count_t[char] naturally returns 0)
            have = count_t[char]
            
            # Step 3: If 't' doesn't have enough, add the difference to our steps
            if needed > have:
                steps += (needed - have)
                
        return steps

# Test
object = Solution()
print(object.minSteps(s = "leetcode", t = "practice")) # Expected Output: 5

# object = Solution()
# print(object.minSteps(s = "leetcode", t = "practice"))

        