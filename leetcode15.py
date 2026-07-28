class Solution:
    def threeSum(self, nums: list[int]) :
        sorted_nums = sorted(nums)
        result = []
        result1 = []


        for i in range(0,len(sorted_nums)-2):
            
            right = len(sorted_nums) - 1
            left = i + 1

            while left < right:
                print(f"i: {i}, left: {left}, right: {right}")
                temp = []
                sum = sorted_nums[i]+sorted_nums[right] + sorted_nums[left]

                if sum > 0:
                    print(f"sum: {sum} > 0, right: {right} -= 1")
                    right -= 1
                elif sum < 0:
                    print(f"sum: {sum} < 0, left: {left} += 1")
                    left += 1

                elif sum == 0:
                    temp.extend([sorted_nums[i],sorted_nums[left],sorted_nums[right]])
                    print(f"sum: {sum} == 0, temp: {temp}, result: {result}")
                    left += 1
                    right -= 1

                sum = 0
                if temp != []:
                    result.append(temp)
            
        for array in result:
            if array not in result1:
                result1.append(array)

        return result1
obj = Solution()
print(obj.threeSum([0.1]))
# [-4,-1,-1,0,1,2]

        