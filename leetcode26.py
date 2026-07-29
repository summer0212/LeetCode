class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        # result = ['_'] * (n)
        result = []

        for i in range(0,n):
            if nums[i] in result:
                continue
            if nums[i] not in result:
                # result[i] = nums[i]
                result.append(nums[i])
        print(f"result: {result}")

        return len(result),result


obj = Solution()
print(obj.removeDuplicates([1,1,2]))