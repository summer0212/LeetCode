class Solution:
    def minElement(self, nums) :
        nums_output = []
        sum = 0

        for i in range(0,len(nums)):
            while nums[i] > 0:
                dig = int(nums[i] % 10)
                # print("dig",dig)
                # print("---------------------------------------")
                sum += dig
                # print("sum",sum)
                # print("---------------------------------------")
                nums[i] = int(nums[i] / 10)
                # print("nums[i]",nums[i])
                # print("---------------------------------------")
            nums_output.append(sum)
            sum = 0
        return min(nums_output)

object = Solution()
print(object.minElement(nums = [999,19,199]))
        