class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(0,len(nums)):
            if nums[right] != 0:
                # Swap the car into the parking spot!
                # (This is Python's 1-line version of your temp variable swap)
                nums[left], nums[right] = nums[right], nums[left]

                left += 1
        return nums
object = Solution()
print(object.moveZeroes(nums = [0,1,0,3,12]))

        