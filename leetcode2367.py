class Solution:
    def arithmeticTriplets(self, nums, diff) -> int:
        num_set = set(nums)
        count = 0

        for i in range(0,len(nums)):
            next_val = nums[i] + diff
            next_next_val = nums[i] + (2* diff)

            if next_val in num_set and next_next_val in num_set:
                count += 1

        return count
    
object = Solution()
print(object.arithmeticTriplets(nums = [0,1,4,6,7,10], diff = 3))
        