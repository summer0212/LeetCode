class Solution:
    def minSubsequence(self, nums) :
        sorted_nums = sorted(nums, reverse=True)
        subsequence_start = []
        subsequence_end = []

        for i in range(0,len(sorted_nums)):
            subsequence_start = sorted_nums[0:i+1]
            subsequence_end = sorted_nums[i+1:len(sorted_nums)]
            # print("End part",subsequence_end)
            if sum(subsequence_start) > sum(subsequence_end):
                return subsequence_start
            subsequence_end = []
            subsequence_start= []

        return []
        
object = Solution()
print(object.minSubsequence(nums = [0]))

        