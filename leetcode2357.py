class Solution:
    def minimumOperations(self, nums) -> int:
        operations = 0

        while True:
            non_zeros_nums = []
            
            for n in nums:
                if n > 0:
                    non_zeros_nums.append(n)

            if len(non_zeros_nums) == 0:
                return operations

            x = min(non_zeros_nums)

            for i in range(len(nums)):
                if nums[i] > 0:
                    nums[i] = nums[i] - x

            operations += 1

        return operations
    
object = Solution()
object.minimumOperations(nums = [1,5,0,3,5])

'''Alternate way:-
The Magic Observation:
Look at the unique positive numbers in the original array: {1, 3, 5}.
There are 3 unique numbers.
The answer is 3.
2. Why does this work?
Every time you subtract the smallest non-zero number (
x
x
), you effectively eliminate that specific value from the array forever.
If you have a 1, and you subtract 1, it becomes 0.
If you have duplicates (like two 5s), they are processed together. When you eventually reduce them to the smallest number, one operation kills both of them.
Conclusion:
The minimum number of operations is simply the count of unique positive integers in the array.

Code:-
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Step 1: Create a set to hold unique positive numbers
        unique_positives = set()
        
        # Step 2: Add only positive numbers to the set
        for num in nums:
            if num > 0:
                unique_positives.add(num)
        
        # Step 3: The result is simply the count of items in the set
        return len(unique_positives)'''