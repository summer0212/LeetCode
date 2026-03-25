class Solution:
    def shuffle(self, nums, n) :
        result = []
        for i in range(n):
            result.append(nums[i])
            print(result)
            result.append(nums[i+n])
            print(result)
        return result
object = Solution()
object.shuffle([1,2,3,4,4,3,2,1], 4)