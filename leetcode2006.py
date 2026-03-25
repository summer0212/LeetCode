class Solution:
    def countKDifference(self, nums, k) :
        count = 0
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                # if nums[i] < nums[j] and abs(nums[i] - nums[j]) == k:
                if abs(nums[i] - nums[j]) == k:
                    count += 1
        return count

object = Solution()
print(object.countKDifference(nums = [3,2,1,5,4], k = 2))
        