class Solution:
    def finalValueAfterOperations(self, operations) :
        ans = 0
        for op in operations:
            if "+" in op:
                ans += 1
            else:
                ans -= 1
        print(ans)
        return ans

object = Solution()
object.finalValueAfterOperations(["x++","x++"])
        