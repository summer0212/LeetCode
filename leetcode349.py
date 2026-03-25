class Solution:
    def intersection(self, nums1, nums2) :
        result = []

        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                if nums1[i] not in result:
                    result.append(nums1[i])

        return result
        
object = Solution()
print(object.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))