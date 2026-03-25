class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        result = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                result += 1
        return result
    
object = Solution()
print(object.numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))