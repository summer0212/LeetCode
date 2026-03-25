class Solution:
    def minimumAverage(self, nums):

        avg = []
        len_of_nums = len(nums)

        # nums.sort()

        for i in range(0,(len_of_nums // 2)):
           max_val = max(nums)
           min_val = min(nums)

           nums.remove(max(nums))
           nums.remove(min(nums))

           calc = (max_val + min_val) / 2
           avg.append(calc)
           print(avg)
        return min(avg)
        


object = Solution()
print(object.minimumAverage(nums = [7,8,3,4,15,13,4,1]))
        