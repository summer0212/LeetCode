class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):
        answer =[]

        for element in range(0,len(r)):
            sub_array = nums[l[element] : r[element] + 1]
            sub_array.sort()
            print(sub_array)

            is_arithmetic = True
            expected_gap = sub_array[1] - sub_array[0]

            for i in range(0,len(sub_array)- 1):
                if sub_array[i+1] - sub_array[i] != expected_gap:
                    is_arithmetic = False
                    break
                
            answer.append(is_arithmetic)
        return answer
    
object = Solution()
print(object.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))
        