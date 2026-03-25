class Solution:
    def removeOuterParentheses(self, s):
        balance_counter = 0
        stack_str = ""

        for char in s:
            if char == "(":
                if balance_counter > 0:
                    stack_str += "("
                balance_counter += 1
            if char == ")":
                balance_counter -= 1
                if balance_counter > 0:
                    stack_str += ")"
        return stack_str

object = Solution()
print(object.removeOuterParentheses(s = "(()())(())(()(()))"))
        