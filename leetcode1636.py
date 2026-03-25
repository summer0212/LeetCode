class Solution:
    def frequencySort(self, nums) :
        nums_dict = {}

        count = 0

        for i in range(0,len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1

            else:
                nums_dict[nums[i]] = 1
        
        def sorting_rules(num):
            return(nums_dict[num], -num)
        
        nums.sort(key=sorting_rules) #The key parameter in sort() tells Python how to sort elements. The key function is applied to each element to determine the sort order.


        return nums

        
object = Solution()
print(object.frequencySort(nums = [2,3,1,3,2]))