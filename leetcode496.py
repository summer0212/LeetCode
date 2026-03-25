class Solution:
    def nextGreaterElement(self, nums1, nums2) :
        result = [-1] * len(nums1)
        print("Result --->", result)

        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                #Finding the position of nums1[i] in nums2 
                index_of_nums1 = nums2.index(nums1[i])
                for j in range(index_of_nums1+1,len(nums2)):
                    if nums2[j] > nums1[i]:
                        result[i] = nums2[j]
                        break
                    # else:
                    #     result.append(-1)

        print(result)
        return result


object =  Solution()
object.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4])
        