class Solution:
    def minOperations(self, nums, k) :
        total = sum(nums)
        if total % k == 0:
            return 0
        else:
            remainder = total % k
            return remainder
        
object = Solution()
print(object.minOperations( nums = [3,2], k = 6))