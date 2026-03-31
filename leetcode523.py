class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        '''Time Exceeded error
        n = len(nums)

        for left in range(n-1):
            sum_window = nums[left]
            
            for right in range(left+1,n):
                
                sum_window += nums[right]

                if sum_window % k == 0:
                    return True
                
        return False'''

        
        # Notebook: {Remainder : Index}
        # Initialize with {0: -1} to catch valid subarrays that start from index 0
        notebook = {0: -1}
        
        running_sum = 0
        
        for i in range(len(nums)):
            # 1. Update running sum
            running_sum += nums[i]
            
            # 2. Find the remainder
            remainder = running_sum % k
            
            # 3. Check our notebook!
            if remainder in notebook:
                # We found a matching remainder! Let's check the length.
                past_index = notebook[remainder]
                
                if (i - past_index) >= 2:
                    return True
                    
            else:
                # 4. ONLY write it down if we haven't seen it before.
                # We want to keep the oldest (smallest) index to maximize length!
                notebook[remainder] = i
                
        # If the loop finishes without returning True, no valid subarray exists.
        return False
    
object = Solution()
print(object.checkSubarraySum(nums = [23,2,6,4,7], k = 13))


        
        