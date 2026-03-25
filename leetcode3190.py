class Solution:
    def minimumOperations(self, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] % 3 == 0:
                continue
            else:
                count += 1
        return count
    
object = Solution()
print(object.minimumOperations([27,90,34,88]))