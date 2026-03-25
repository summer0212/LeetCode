from unittest import result


class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)

        for i in range(0,n+1):
            if i not in sorted_nums:
                result = i

        return result

object = Solution()
print(object.missingNumber(nums = [0,1]))