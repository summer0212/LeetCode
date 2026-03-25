class Solution:
    def findIntersectionValues(self, nums1, nums2) :
        result = []
        count_of_nums1 = 0
        count_of_nums2 = 0

        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                count_of_nums1 += 1
        result.append(count_of_nums1)
        
        for j in range(0,len(nums2)):
            if nums2[j] in nums1:
                count_of_nums2 += 1
        result.append(count_of_nums2)
        return result

        #One liner using list comprehension
        #return[sum(n in nums2 for n in nums1),sum(n in nums1 for n in nums2)]
        
object = Solution()
print(object.findIntersectionValues(nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]))

        