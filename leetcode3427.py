class Solution:
    def subarraySum(self, nums):
        total = 0
        result = 0
        i = 0
        while 0<=i<len(nums):
            start = max(0,i - nums[i])
            # print(start)
            end = i + 1

            subarray = nums[start : end]
            print(subarray)
            total = sum(subarray)
            print(total)
            result = result + total
            subarray = []
            i +=1

        print(result)

object = Solution()
object.subarraySum(nums = [2,3,1])
        