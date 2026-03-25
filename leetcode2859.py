class Solution:
    def sumIndicesWithKSetBits(self, nums, k) :
        total = 0
        for i in range(0,len(nums)):
            # bin_str = bin(num).count('1')
            # print(bin_str)
            if bin(i).count('1') == k:
                total = total + nums[i]
        return total

        
object = Solution()
print(object.sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1))