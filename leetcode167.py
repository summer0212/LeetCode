class Solution:
    def twoSum(self, numbers, target: int) :
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left+1,right+1]
            
            elif current_sum < target:
                left += 1
            
            else:
                right -= 1

        
object = Solution()
print(object.twoSum(numbers = [2,7,11,15], target = 9))
        