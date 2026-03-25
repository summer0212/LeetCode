class Solution:
    def heightChecker(self, heights) -> int:

        expected = sorted(heights)
        count = 0

        for i in range(0,len(heights)):
            if heights[i] != expected[i]:
                count += 1

        return count

object = Solution()
print(object.heightChecker(heights = [1,2,3,4,5]))
        