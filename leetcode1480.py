class Solution:
    def runningSum(self, nums) :
        running_sum = []
        previous_sum = 0

        for i in range(0,len(nums)):
            previous_sum = previous_sum + nums[i]
            # print(previous_sum)
            running_sum.append(previous_sum)
        # print(running_sum)
        return running_sum
    
object = Solution()
nums = [1,2,3,4]
print(object.runningSum(nums))
        