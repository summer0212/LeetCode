from collections import Counter

'''class Solution:
    def intersect(self, nums1, nums2) :
        nums1_freq = Counter(nums1)
        result = []

        for i in range(0,len(nums2)):
            if nums2[i] in nums1_freq and nums1_freq[nums2[i]] > 0:
            # if  nums1_freq[nums2[i]] > 0:

                # print("Checking values", nums1_freq[nums2[i]])
                result.append(nums2[i])
                nums1_freq[nums2[i]] -= 1
                # print("Printing freq dict after deduction in value",nums1_freq)

        print("Printing Result",result)'''

class Solution:
    def intersect(self,nums1,nums2):
        nums1_freq = Counter(nums1)
        result = []

        for num in nums2:
            if nums1_freq[num] > 0:
                result.append(num)
                nums1_freq[num] -=1
        return result

object =  Solution()
print(object.intersect(nums1 = [1,2,2,1], nums2 = [2,2,2]))

        