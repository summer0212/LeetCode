from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
            return False
        
        s1_dict = Counter(s1)
        window_dict = Counter(s2[:k])

        if s1_dict == window_dict:
            return True

        for left in range(1,len(s2) - k + 1):
            char_out = s2[left - 1]
            char_in = s2[left + k - 1]

            window_dict[char_out] -= 1
            if window_dict[char_out] == 0:
                del window_dict[char_out]

            window_dict[char_in] += 1

            if s1_dict == window_dict:
                return True
        return False
    
object = Solution()
print(object.checkInclusion(s1 = "ab", s2 = "eidboaooo"))
        
        