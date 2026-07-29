
class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}

        for i in range(0,len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1

        for key in s_dict:
            if s_dict[key] == 1:
                return s.index(key)
        return -1
obj = Solution()
print(obj.firstUniqChar("aabb"))