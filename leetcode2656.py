class Solution:
    def maximizeSum(self, nums, k: int) -> int:
        sorted_nums = sorted(nums)
        score = 0

        while k > 0:
            score += sorted_nums[-1]
            sorted_nums[-1] = sorted_nums[-1] + 1
            k -= 1
        
        return score
    
object = Solution()
print(object.maximizeSum(nums = [1,2,3,4,5], k = 3))