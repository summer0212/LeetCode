class Solution:
    def arrayPairSum(self, nums) :
        sorted_nums = sorted(nums)
        
        result = 0

        for i in range(0,len(sorted_nums), 2):
            result += sorted_nums[i]

        return result

object = Solution()
print(object.arrayPairSum(nums = [6,2,6,5,1,2]))
        