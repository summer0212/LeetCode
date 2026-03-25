class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(0,len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                current_window_size = right - left + 1
                min_length = min(min_length,current_window_size)

                current_sum -= nums[left]

                left += 1

        if min_length == float('inf'):
            return 0
        else:
            return min_length
        
object = Solution()
print(object.minSubArrayLen(target = 7, nums =[2, 3, 1, 2, 4, 3]))

'''Note :- Why this is a Superpower
Because you used a while loop to catch up, the left pointer only ever moves forward. It never resets. This means even though there is a loop inside a loop, both pointers only travel across the array exactly one time. The Time Complexity is an incredibly fast 
O(N) !'''