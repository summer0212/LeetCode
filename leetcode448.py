class Solution:
    def findDisappearedNumbers(self, nums) :
        nums_set = set(nums)

        result = []

        for i in range(1,len(nums)+1):
            if i not in nums_set:
                result.append(i)

        return result
    
object = Solution()
print(object.findDisappearedNumbers(nums = [1,1]))
        