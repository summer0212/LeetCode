class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        current_window_sum = sum(nums[0:k])
        right = k
        total_sum = [current_window_sum]

        for i in range(1,len(nums) - k + 1): #6-4+1
            current_window_sum = current_window_sum - nums[i-1]+nums[right]
            total_sum.append(current_window_sum)
            right += 1
            
        max_sum = max(total_sum)
        return max_sum/k



obj = Solution()
print(obj.findMaxAverage(nums = [5], k = 1))

'''Alternate method:- 
     left = 0
        
        current_sum = sum(nums[left:k])
        
        max_sum = [current_sum]
        
        
        for left in range(1,(len(nums) - k + 1)):
            right = left + k -1
           
            current_sum = current_sum + nums[right] - nums[left - 1]
            max_sum.append(current_sum)
            
        total_sum = max(max_sum)
        return total_sum / k'''