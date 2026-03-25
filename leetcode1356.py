class Solution:
    def sortByBits(self, arr) :
    # We define a helper rule (key) for the sort function
        # This function takes a number and returns a tuple: (bit_count, value)
        def sorting_rule(num):
            #Get the binary string for the number
            binary_string = bin(num)

            #2. Count the 1's
            count_ones = binary_string.count("1")

            #3. Return the tuple for the comparison
            #Primary : count_ones , Secondary: num
            return (count_ones,num)
        
        #Apply sorting using the rule
        arr.sort(key=sorting_rule)
        return arr

object = Solution()
object.sortByBits(arr = [0,1,2,3,4,5,6,7,8])
        