class Solution:
    def pivotIndex(self, nums) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(0,len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if right_sum == left_sum :
                return i
            
            left_sum += nums[i]

        return -1
    
object = Solution()
print(object.pivotIndex(nums = [2,1,-1]))
        