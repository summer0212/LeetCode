


class Solution:
    def earliestTime(self, tasks):
        result = sum(tasks[0])
        # temp = 0
        finishing_time = 0

        if len(tasks) == 1:
            return sum(tasks[0])

        for i in range(0,len(tasks)):
            finishing_time = sum(tasks[i])
            if result > finishing_time:
                result = finishing_time

        return result

object = Solution()
print(object.earliestTime( tasks = [[1,6],[2,3]]))




        