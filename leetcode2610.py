class Solution:
    def findMatrix(self, nums) :
        dict ={}

        for i in range(0,len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        
        # two_d_row_val = max(dict, key=dict.get)
        two_d_row_val = max(dict.values())
        two_d_array = [[0] for _ in range(two_d_row_val)] #[[0], [0], [0]]
        # print(two_d_array)
        two_d_array[0]=list(dict.keys())
        # print(two_d_array)


object = Solution()
object.findMatrix(nums = [1,3,4,1,2,3,1])