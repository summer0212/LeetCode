class Solution:
    def smallerNumbersThanCurrent(self, nums) :
        count_list = []
        count = 0
        for i in range(0,len(nums)):
            count = 0
            for j in range(0,len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            count_list.append(count)
        print(count_list)
        return count_list
    
object = Solution()
object.smallerNumbersThanCurrent([7,7,7,7])
        