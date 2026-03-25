class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans = ""
        for char in address:
        # for i in range(len(address)):
            if char == '.':
                ans += "[.]"
            else:
                ans += char
        return ans
    
object = Solution()
print(object.defangIPaddr("1.1.1.1"))