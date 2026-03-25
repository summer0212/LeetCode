class Solution:
    def xorOperation(self, n, start):
        nums = []
        result = 0
        for i in range(0,n):
            calculation = start + 2 *i
            nums.append(calculation)
            calculation = 0
        print(nums)

        for j in range(0, len(nums)):
            result = result ^ nums[j]
        print(result)
        return result

object = Solution()
n=4
start = 3
object.xorOperation(n,start)