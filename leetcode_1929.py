class Solution:
    def getConcatenation(self, nums) :
        # new_num = nums + nums
        # print(new_num)
        # length = len(nums)
        # ans = list(range(2*length))
        # for i in range(len(nums)):
        #     ans[i] = nums[i]
        #     ans[i+length] = nums[i]
        # return ans
        return nums + nums
    
object = Solution()
print(object.getConcatenation([1, 2, 1]))