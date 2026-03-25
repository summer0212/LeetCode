class Solution:
    def decompressRLElist(self, nums) :
        decompressed_list = []
        final_list = []
        for i in range(0,len(nums),2):
            print("i",i)
            temp_val = []
            for j in range(0,nums[i]):
                print("j",j)
                temp_val.append(nums[i+1])
            decompressed_list.append(temp_val)
        for item in decompressed_list:
            final_list.extend(item)
        return final_list



object=Solution()
print(object.decompressRLElist([1,2,3,4]))



