class NumArray():
    def __init__(self,nums):
        # self.prefix_sum = []
        n = len(nums)
        self.prefix_sum = [0] * (n + 1)
        current = 0
        self.prefix_sum[0] = nums[0]

        for i in range(0,len(nums)-1):
            # current += nums[i]
            # self.prefix_sum.append(current)
            self.prefix_sum[i+1] = self.prefix_sum[i] + nums[i+1]

    def sumRange(self,left,right):
        if left > right:
            return None
        if left == 0:
            return self.prefix_sum[right]
        else:
            ans = self.prefix_sum[right] - self.prefix_sum[left - 1]
            return ans
        
object = NumArray([-2,0,3,-5,2,-1])
print(object.sumRange( 2,5))

    