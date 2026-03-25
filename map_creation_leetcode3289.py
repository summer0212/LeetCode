class Solution:
    def getSneakyNumbers(self, nums):
        count_dict = {}
        result = []
        for element in nums:
            if element in count_dict:
                count_dict[element] += 1
            else:
                count_dict[element] = 1
        
        for key,value in count_dict.items():
            if value > 1:
                result.append(key)
        return result
        
object = Solution()
print(object.getSneakyNumbers([0,3,2,1,3,2]))

'''Alternative way:
def findRepeated(nums):
    seen = set()
    repeated = set()
    
    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
    
    return list(repeated)
'''