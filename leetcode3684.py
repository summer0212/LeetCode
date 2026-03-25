class Solution:
    def maxKDistinct(self, nums, k: int) :
        unique_nums = list(set(nums))
        print("----------unique_nums-----------",unique_nums)
        sorted_nums = sorted(unique_nums,reverse=True)
        print("----------sorted_nums-----------",sorted_nums)

        trim_nums = sorted_nums[0:k]
        
        return trim_nums

object= Solution()
print(object.maxKDistinct(nums = [84,93,100,77,93], k = 3))
        