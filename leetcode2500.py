class Solution:
    def deleteGreatestValue(self, grid) :
        sum = 0
        temp = []

        '''while grid is not None: This will not work as this loop will run even if we have [[],[]]'''
        while len(grid[0]) > 0:
            for i in range(0,len(grid)):
                temp.append(max(grid[i]))
                index_of_max = grid[i].index(max(grid[i]))
                grid[i].pop(index_of_max)

            print("Printing the temp befor emptying",temp)
            sum += max(temp)
            print("SUM for the first loop after which the elemnts are decreasing",sum)
            temp = []
            print("-"* 20)
        return sum
    
'''Step 2: Using sorted()
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # Step 1: Sort each row
        for row in grid:
            row.sort()
            
        total_sum = 0
        
        # Step 2: Iterate through columns
        # len(grid[0]) gives the number of columns
        for j in range(len(grid[0])):
            column_values = []
            
            # Step 3: Iterate through rows to collect the column's values
            for i in range(len(grid)):
                column_values.append(grid[i][j])
                
            # Step 4: Add max of this column to total
            total_sum += max(column_values)
            
        return total_sum'''

object = Solution()
object.deleteGreatestValue(grid = [[1,2,4],[3,3,1]])

        


        