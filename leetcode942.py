class Solution:
    def diStringMatch(self, s: str) :
        low = 0
        high = len(s) # The highest number is equal to length of string
        result = []
        
        # Loop through every character in the string
        for char in s:
            if char == 'I':
                # 'I' means we need to go up next time.
                # So we put the smallest number now.
                result.append(low)
                low += 1
            else:
                # 'D' means we need to go down next time.
                # So we put the largest number now.
                result.append(high)
                high -= 1
        
        # After the loop, one number is always left over. 
        # (low and high will be equal here)
        result.append(low)
        
        return result

object = Solution()
print(object.diStringMatch(s="III"))