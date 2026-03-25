class Solution:
    def leftRightDifference(self, nums):
        answer = []
        difference = 0
        for i in range(len(nums)):
            left_sum_val = 0
            for j in range(0,i):
                left_sum_val += nums[j] 
            
            right_sum_val = 0
            for k in range(i+1, len(nums)):
                right_sum_val += nums[k]
            
            difference = abs(left_sum_val - right_sum_val)

            answer.append(difference)
        return answer
        
object =Solution()
print(object.leftRightDifference(nums = [10,4,8,3]))

        