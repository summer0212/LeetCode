class Solution:
    def maxProductDifference(self, nums) :
        '''
        problem with below Solution:
        The reason you are getting a Memory Limit Exceeded (MLE) error is that you are generating every possible pair of numbers.

        
        multiplied_val = []

        for i in range(0 ,len(nums)):
            for j in range(i+1, len(nums)):
                multiplied_val.append(nums[i] * nums[j])

        # for k in range(0,len(multiplied_val)):
        #     result = abs(multiplied_val(i) - multiplied_val(i+1))
        #     prev = result
        #     if prev > res:

        # print( multiplied_val)

        result = max(multiplied_val) - min(multiplied_val)
        print(result)'''

        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        result = abs((sorted_nums[0] * sorted_nums[1]) - (sorted_nums[n-1] * sorted_nums[n-2]))
        print(result)

object = Solution()
object.maxProductDifference(nums = [5,6,2,7,4])