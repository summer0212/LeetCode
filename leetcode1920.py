class Solution:
    def buildArray(self, nums) :
        ans = []

        for i in range(0,len(nums)):
            # print(nums[i])
            ans.append(nums[nums[i]])
        return ans



object = Solution()
print(object.buildArray(nums = [0,2,1,5,3,4] ))
        