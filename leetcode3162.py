class Solution:
    def numberOfPairs(self, nums1, nums2, k) :
        count = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                divisible_val= nums2[j] * k
                if nums1[i] % divisible_val == 0:
                    count += 1

        return count

object = Solution()
print(object.numberOfPairs(nums1 = [1,3,4], nums2 = [1,3,4], k = 1))
        