class Solution():
    def largestAlt(self,gains):
        n = len(gains)
        prefix_gain_list = [0] * (n)
        prefix_gain_list[0] = gains[0]

        for i in range(0,n-1):
            prefix_gain_list[i+1] = prefix_gain_list[i] + gains[i+1]

        return max(prefix_gain_list)

obj = Solution()
print(obj.largestAlt([-4,-3,-2,-1,4,3,2]))
