class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        left = 1

        for right in range(1,n):
            if nums[right] != nums[right-1]:
                nums[left]  = nums[right]
                left += 1
        return left
        


obj = Solution()
print(obj.removeDuplicates([1,1,2]))