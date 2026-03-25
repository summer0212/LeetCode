class Solution:
    def balancedStringSplit(self, s) :
        split_count = 0
        balance_count = 0

        for char in s:
            if char == "R":
                balance_count +=1
            elif char == "L":
                balance_count -= 1
            if balance_count == 0:
                split_count += 1
        return split_count
    
''' Alternate logic:
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        output = 0
        r_count = 0
        l_count = 0
        
        for char in s:
            if char == "R":
                r_count +=1

            elif char == "L":
                l_count += 1

            if r_count == l_count:
                output += 1
                r_count = 0
                l_count = 0

        return output'''
    
object = Solution()
print(object.balancedStringSplit("LLLLRRRR"))
        