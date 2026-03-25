class Solution:
    def getFinalState(self, nums, k, multiplier):
        min_val = 0
        for i in range(0,k):
            min_val = min(nums)
            index_of_min_val = nums.index(min_val)
            nums[index_of_min_val] = nums[index_of_min_val] * multiplier
        return nums
            

# Example test
my_nums = [2, 5, 1, 8, 1]
k_ops = 3
mult = 10
object = Solution()
print(object.getFinalState(my_nums, k_ops, mult))