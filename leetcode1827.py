'''This is a classic Greedy Algorithm problem.
                                               The Logic: "The Staircase"
Explanation :- Imagine the array is a staircase. To be "strictly increasing," every step must be at least 1 unit higher than the step before it.
Step 0: We never touch the first number. Why? Because making the first number bigger only makes our job harder for the rest of the numbers. Keep it as small as possible.
Step 1: Look at the current number (current) and the previous number (prev).
Scenario A: If current > prev, we are good! Do nothing.
Scenario B: If current <= prev, we have a problem. The step is too low.
The Strategy:
If current <= prev, we must increase current.
To save operations (minimum moves), we shouldn't make current huge. We should make it exactly 1 unit higher than prev.
Formula:
New Value=Previous Value+1
Operations Needed=New Value−Old Value
'''



class Solution:
    def minOperations(self, nums) -> int:
        operations = 0

        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                diff = abs(nums[i]-nums[i-1])
                diff += 1
                # Error statmemnt :- operations += (diff+1)
                operations += diff
                nums[i]= nums[i] + diff
        print("Printing the new list everytime",nums)
        return operations

'''ALternate logic:
output = 0
        steps = 0
        
        for i in range(0,len(nums)-1):
            if nums[i] < nums[i+1]:
                continue
            else:
                temp = nums[i+1]
                nums[i+1] = nums[i] + 1
                steps = nums[i+1] - temp
                output += steps
            steps = 0
        return output'''
object = Solution()
print(object.minOperations(nums = [1,5,2,4,1]))

        