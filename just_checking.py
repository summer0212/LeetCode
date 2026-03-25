class Solution:
    def findMatrix(self, nums) :
        # This will hold our final 2D array
        result =[]
        
        # This is our Hash Table to track "How many times have I seen num?"
        counts = {}
        
        for num in nums:
            # 1. Get the current count of this number (default is 0)
            row_index = counts.get(num, 0)
            print("Row Index",row_index)
            
            # 2. If our result 2D array doesn't have this row yet, create it!
            if row_index == len(result):
                result.append([])
                
            # 3. Add the number to its designated row
            result[row_index].append(num)
            
            # 4. Update the hash table so the next time we see this number, 
            # it goes to the next row down.
            counts[num] = row_index + 1
            
        return result

object = Solution()
object.findMatrix(nums = [1,3,4,1,2,3,1])