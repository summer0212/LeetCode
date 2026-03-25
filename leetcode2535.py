from unicodedata import digit


class Solution:
    def differenceOfSum(self, nums) -> int:
        nums_total = sum(nums)
        print("total of all elements:", nums_total)

        digit_total = 0

        # Converting the int-array into str-array
        str_array = [str(num) for num in nums]
        concat_str = "".join(str_array)

        value = int(concat_str)

        while value != 0:
            dig = int(value % 10)
            digit_total += dig
            value = value//10

        print(digit_total)

        return abs(nums_total - digit_total)
  


object = Solution()
print("Final answer",object.differenceOfSum(nums = [3,6,15,14,17,12,9,9,15,3,13,5,18,13,18,17,5,14,7,20]))
        