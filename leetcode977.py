class Solution:
    def sortedSquares(self, nums):
        result = []

        for num in nums:
            result.append(num ** 2)

        # print(sorted(result))
        return sorted(result)
    
object = Solution()
print(object.sortedSquares(nums = [-4,-1,0,3,10]))
        