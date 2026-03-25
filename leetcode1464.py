# from audioop import mul


class Solution:
    def maxProduct(self, nums) :
        maximum_val = 0
        multiplied_val = 0

        for i in range(0,len(nums) - 1):
            for j in range(i+1, len(nums)):
                print("------Multilpied value before------", multiplied_val)
                multiplied_val = int((nums[i] - 1) * (nums[j] - 1))
                print("------Multilpied value after------", multiplied_val)

                if multiplied_val > maximum_val:
                    maximum_val = multiplied_val

        return maximum_val
        
object = Solution()
print(object.maxProduct(nums =[3,7]))