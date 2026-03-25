class Solution:
    def topKFrequent(self, nums, k: int) :
        dict = {}

        for i in range(0,len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        ''' Wrong options:
        result = sorted(dict.values(),reverse=True)
        -->result = [2, 2, 1, 1, 1]
        # ✗ Problem: You lose which KEY has which frequency!
        
        result = sorted(dict.keys(),reverse=True)
        --># Sorts the KEYS by their numeric value (descending)
            result = [4, 3, 2, 1, -1]
            # ✗ Problem: Ignores frequencies completely!

        result = sorted(dict.keys())
        --> # Sorts the KEYS by their numeric value (ascending)
        result = [-1, 1, 2, 3, 4]
        # ✗ Problem: Still ignores frequencies!'''
        
        result = sorted(dict, key = dict.get, reverse=True)
        #Key insight: Use key=dict.get to sort keys based on their values (frequencies) in descending order!


        print("result",result)
        return result[:k]

object = Solution()
print(object.topKFrequent(nums = [4,1,-1,2,-1,2,3], k = 2))