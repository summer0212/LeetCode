class Solution:
    def transformArray(self, nums) :
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        print(nums)
        nums.sort()  # Sort in-place
        return nums  # Return the sorted list

object = Solution()
print(object.transformArray([4,3,2,1]))