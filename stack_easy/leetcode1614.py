class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        balance_counter = 0

        for char in s:
            if char == '(':
                balance_counter += 1
                max_depth = max(max_depth,balance_counter)

            if char == ")":
                balance_counter -= 1

        return max_depth

object = Solution()
print(object.maxDepth(s = "(1)+((2))+(((3)))"))