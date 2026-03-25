class Solution:
    def stableMountains(self, height, threshold) :
        stable_mt_index = []
        for h in range(1,len(height)):
            if height[h - 1] > threshold:
                stable_mt_index.append(h)
        return stable_mt_index

object = Solution()
print(object.stableMountains( height = [1,2,3,4,5], threshold = 2))        