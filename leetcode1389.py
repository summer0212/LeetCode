class Solution:
    def createTargetArray(self, nums, index) :
        target = []
        for i in range(0,len(nums)):
            value_to_insert = nums[i]
            insertion_index = index[i]
            target.insert(insertion_index,value_to_insert)
        return target

object = Solution()
print(object.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
        