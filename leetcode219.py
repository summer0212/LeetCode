from collections import Counter
'''Note:= I found an issue with enumerate
for i,num in enumerate(nums): - for this statement the error was - TypeError: 'int' object is not iterable because enumerate can take only iterables as its parameters. So i had
to change the 0,len(nums) as only nums because nums is a list.'''
class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        #Dictionary to store the {Number : Index value}
        seen_indices = {}

        for i,num in enumerate(nums):
            #1. Check if we have seen this number before in the list
            if num in seen_indices:
                prev_index = seen_indices[num]

                #Formula : abs(i-j) <= k
                if i-prev_index <= k:
                    return True

            #Updating the dict with the current index value of the number
            ## This handles both new numbers AND updating old numbers to the new position
            seen_indices[num] = i

        return False


object = Solution()
print(object.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))

"""Alternate methods:
FIRST - Logic correct but Time limit exceeded
 # for left in range(0,len(nums)):
        #     right = left + 1
        #     while right < len(nums):
        #         if nums[left] == nums[right] and abs(left-right) <= k:
        #             return True
        #         right += 1
                
        # return False

#--------Alternate right method-----------
🟢 SECOND Logic:-
        nums_dict = {}
                
        for i in range(0,len(nums)):
            if nums[i] in nums_dict:
                past_index = nums_dict[nums[i]]
                
                if abs(i - past_index) <= k:
                    return True
                else:
                    nums_dict[nums[i]] = i
                    
            else:
                nums_dict[nums[i]] = i
        
                
        return False"""


        