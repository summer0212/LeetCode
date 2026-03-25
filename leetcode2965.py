class Solution:
    def findMissingAndRepeatedValues(self, grid) :
        flatten_ar = []
        ans = []
        frequency_of_element = {}
        count = 0

        for i in range(0,len(grid)):
            for j in range(0, len(grid[i])):
                flatten_ar.append(grid[i][j])
        flatten_ar.sort()
        # print(flatten_ar)
        

        for i in range(0,len(flatten_ar)):
            if flatten_ar[i] in frequency_of_element:
                frequency_of_element[flatten_ar[i]] += 1
            else:
                frequency_of_element[flatten_ar[i]] = 1

        # Find key with maximum value
        # print(frequency_of_element.get)
        max_key = max(frequency_of_element, key=frequency_of_element.get) #frequency_of_element.get is a method that gets the value for each key
        ans.insert(0, max_key)
        # print(ans)

        #--------Solving the second part-------------
        n = len(flatten_ar)
        expected_elements = set(range(1,n+1))
        actual_elements = set(flatten_ar)
        missing = expected_elements - actual_elements
        missing_element = list(missing)[0]

        ans.insert(1, missing_element)


        return ans

        


object = Solution()
print(object.findMissingAndRepeatedValues(grid =[[9,1,7],[8,9,2],[3,4,6]]))