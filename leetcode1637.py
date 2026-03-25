class Solution:
    def maxWidthOfVerticalArea(self, points) :
        new_list = []
        sorted_list = []
        diff = 0
        for i in range(0,len(points)):
            # for j in points[i]:
            new_list.append(points[i][0])
        sorted_list = sorted(new_list)
        for j in range(0,len(sorted_list)-1):
            temp_diff = abs(sorted_list[j] - sorted_list[j+1])
            if temp_diff > diff:
                diff = temp_diff
        # print(diff)
        return diff

        # print(new_list)

object = Solution()
object.maxWidthOfVerticalArea([[3,1], [9,0], [1,0], [1,4], [5,3], [8,8]])