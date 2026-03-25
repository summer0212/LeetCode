class Solution:
    def smallestEvenMultiple(self, n) :
        if n % 2 == 0:
            return n
        else:
            return 2 * n
        
object = Solution()
print(object.smallestEvenMultiple(6))