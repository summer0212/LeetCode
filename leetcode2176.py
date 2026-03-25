# from nt import cpu_count


class Solution:
    def countPairs(self, nums, k) :
        count = 0
        
        for i in range(0,len(nums)-1):
            for j in range((i+1),len(nums)):
                if nums[i] != nums[j]:
                    continue
                elif nums[i] == nums[j] and int(i*j) % k == 0:
                    count += 1

        return count

object = Solution()
print(object.countPairs(nums = [3,1,2,2,2,1,3], k = 2))
        