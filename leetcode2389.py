import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Step 1: Sort the nums (Cheapest items first)
        nums.sort()
        
        # Step 2: Build the Prefix Sum array (Running totals)
        # We modify nums in-place to save space
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        
        # Now nums looks like: [Sum of 1 item, Sum of 2 items, Sum of 3 items...]
        
        answer = []
        
        # Step 3: Answer each query
        for budget in queries:
            # bisect_right finds the insertion point to maintain sorted order.
            # Ideally, it tells us "How many numbers in this list are <= budget"
            count = bisect.bisect_right(nums, budget)
            answer.append(count)
            
        return answer