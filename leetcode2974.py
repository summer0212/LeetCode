class Solution:
    def numberGame(self, nums) :
        alice = 0
        bob = 0
        arr = []
        i = 0
        nums.sort()
        # print(nums)
        # while i < len(nums), this is wrong condition, it does not iterate nums correctly, or (while nums) this checks until the nums is not empty:
        while len(nums) > 0:
            alice = nums[0]
            bob = nums[1]
            arr.append(bob)
            arr.append(alice)

            nums.remove(alice)
            nums.remove(bob)
            # print(nums)

            alice = 0
            bob = 0
            i += 1
        return arr


object = Solution()
print(object.numberGame( nums = [2,7,9,6,4,6]))
            
        