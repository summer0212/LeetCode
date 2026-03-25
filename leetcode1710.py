class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        '''Explaining the sorting mechanism: I want to sort as per the second element of the inner array
        Imagine you are a truck driver. You have limited space on your truck; you can only carry Kboxes (truckSize).
You arrive at a warehouse, and there are different piles of boxes.
        Pile A: 10 boxes. Each box contains 1 unit of gold.
        Pile B: 5 boxes. Each box contains 10 units of gold.
        Pile C: 8 boxes. Each box contains 5 units of gold.
        Your Goal: Drive away with the maximum amount of gold possible.
How do you choose?
        You don't care which pile is the biggest. You care about density (value per box).
        First Choice: You will aggressively take every single box from Pile B because they are worth the most (10 units each).
        Second Choice: If you still have space, you move to Pile C (5 units each).
        Last Choice: If you still have space, you take from Pile A (1 unit each).
The Algorithm:
        Sort the box types based on "Units per Box" (Largest to Smallest).
        Iterate through the sorted list.
        Fill the truck with as many of the current high-value boxes as possible.
        Stop when the truck is full.'''
        
        sorted_boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse=True) # x is like the i-> the iteration number = 0,1,2...
        '''Step-by-step execution:

            sorted() picks the first element [3, 1] and passes it to lambda:

            lambda x: x[1] → lambda [3, 1]: [3, 1][1] → returns 1
            sorted() picks the second element [1, 2] and passes it to lambda:

            lambda x: x[1] → lambda [1, 2]: [1, 2][1] → returns 2
            sorted() picks the third element [2, 0] and passes it to lambda:

            lambda x: x[1] → lambda [2, 0]: [2, 0][1] → returns 0'''
        
        total_units = 0
        for numberOfBoxesi, numberOfUnitsPerBoxi in sorted_boxTypes:

            if truckSize >= numberOfBoxesi:
                total_units += numberOfBoxesi * numberOfUnitsPerBoxi
                truckSize -= numberOfBoxesi

            else:
                # Take only what fits (which is exactly truckSize)
                total_units += truckSize * numberOfUnitsPerBoxi
                # The truck is now full, we can stop immediately
                return total_units
            
        return total_units
    
object = Solution()
print(object.maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))
            