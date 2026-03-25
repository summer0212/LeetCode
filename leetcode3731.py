class Solution:
    def findMissingElements(self, nums) :
        sorted_nums = sorted(nums)
        start = sorted_nums[0]
        end = sorted_nums[-1]
        result = []

        for i in range(start,end+1):
            if i not in sorted_nums:
                result.append(i)
        '''One liner -> return[i for i in range(start,end+1)if i not in sorted_nums]'''

        return result

object = Solution()
print(object.findMissingElements(nums = [5,1]))