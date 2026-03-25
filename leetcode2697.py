
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)
        n = len(s_list)

        for i in range(0, n//2):
            j = -(i+1)

            if s_list[i] != s_list[j]:

                smaller_char = min(s_list[i], s_list[j])

                s_list[i] = smaller_char
                s_list[j] = smaller_char

        return "".join(s_list)
    
object = Solution()
print(object.makeSmallestPalindrome(s = "abcd"))
