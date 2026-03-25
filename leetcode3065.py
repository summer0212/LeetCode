class Solution:
    def minOperations(self, nums, k) :
        count = 0
        # nums = sorted(nums)
        nums.sort()
        for num in nums:
            if num < k:
                count += 1
                # nums.remove(nums[i])
            else: 
                break
        return count
    
object =  Solution()
print(object.minOperations(nums = [2,11,10,1,3], k = 10))
        

