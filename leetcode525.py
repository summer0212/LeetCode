class Solution:
    def findMaxLength(self, nums) -> int:
        notebook = {0:-1}
        running_sum = 0
        max_length = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                running_sum += 1

            else:
                running_sum -= 1

            if running_sum in notebook:
                past_index = notebook[running_sum]
                current_length = i - past_index
                max_length = max(max_length,current_length)            

            else:
                notebook[running_sum] = i

        return max_length
    
object = Solution()
print(object.findMaxLength(nums = [0,1,0]))