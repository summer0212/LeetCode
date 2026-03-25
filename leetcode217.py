class Solution:
    def containsDuplicate(self, nums) -> bool:
        set_of_nums = set(nums)

        # print("NUMS alone",nums)
        # print("NUMS set",set_of_nums)

        if len(nums) != len(set_of_nums):
            return False
            
        return True

object = Solution()
print(object.containsDuplicate(nums = [1,2,3,4]))

'''Ways to find duplicate -> Other methods ->
1.Logic:
Imagine you are checking IDs at a door. You have a blank notebook (seen).
code
Python
def containsDuplicate(nums):
    seen = set()
    
    for num in nums:
        # Check if we have seen it before
        if num in seen:
            return True
        # Mark it as seen
        seen.add(num)
        
    return False
    
    2. Logic:
Use collections.Counter. It builds a dictionary of counts instantly. This means by creating the dict and counting there frequency
from collections import Counter

def findDuplicates(nums):
    # 1. Count everything: [1, 2, 2, 3] -> {1:1, 2:2, 3:1}
    counts = Counter(nums)
    
    # 2. Extract numbers with count > 1
    # .items() gives us pairs like (number, frequency)
    result = [num for num, freq in counts.items() if freq > 1]
    
    return result'''
